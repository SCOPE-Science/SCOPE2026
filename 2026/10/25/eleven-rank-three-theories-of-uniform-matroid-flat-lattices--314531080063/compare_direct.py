"""Check two independent exact signatures for minimal representatives."""
from verify_types import complete_type

def signature(n,r):
    return {','.join(str(65536*kind+mask) for kind,mask in sorted(row))+',' for row in complete_type(n,r)}

count=0
with open('verify_direct_output.txt',encoding='utf-8') as inp:
    for line in inp:
        if not line.startswith('n='):
            continue
        header,entries=line.rstrip('\n').split(' codes=',1)
        fields=dict(item.split('=') for item in header.split() if '=' in item)
        n,r=int(fields['n']),int(fields['r'])
        direct=set(entries.split('|'))-{''}
        assert direct==signature(n,r),(n,r)
        count+=1
assert count==12,count
print('DIRECT_ORBIT_SIGNATURE_AGREEMENT_OK representatives=12')
