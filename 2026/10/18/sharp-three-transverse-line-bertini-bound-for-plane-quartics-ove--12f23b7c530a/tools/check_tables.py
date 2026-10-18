"""Compare every hardcoded exhaustive-enumeration lookup against independent Python-generated tables."""
import ast,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
source=(ROOT/'tools/plane_quartic_orbits.cpp').read_text()
data=json.loads((ROOT/'data/quartic_tab.json').read_text())
gens=json.loads((ROOT/'data/qgenmat.json').read_text())
def parse(name):
    mat=re.search(r'static const uint8_t '+re.escape(name)+r'\s*=\s*(\{.*?\});',source,re.S)
    assert mat,name
    return ast.literal_eval(mat.group(1).replace('{','[').replace('}',']'))
good=parse('good[243]')
tab=parse('tab[13][3][243]')
trans=parse('trans[5][15][15]')
assert len(good)==243 and len(tab)==13 and len(trans)==5
for n in range(243):
    j=sum(((n//3**i)%3)*3**(4-i) for i in range(5))
    assert good[n]==data['good'][j],('good',n)
for l in range(13):
 for j in range(3):
  for n in range(243):
   result=sum((sum(data['mat'][l][j*5+k][r]*((n//3**k)%3) for k in range(5))%3)*3**r for r in range(5))
   assert tab[l][j][n]==result,(l,j,n)
assert trans==gens
print('PASS all 243 good values, all 9477 line-restriction values, all 1125 GL3-action entries')
