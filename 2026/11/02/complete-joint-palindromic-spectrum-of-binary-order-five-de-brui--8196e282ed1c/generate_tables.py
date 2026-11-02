"""Generate three finite data tables from the independent Euler-tour traversal."""
from collections import Counter
from pathlib import Path
from checker import rooted_euler_cycles, palindromes_via_windows, spectrum

rows=[]; joint=Counter();prof=Counter()
for word in sorted(set(rooted_euler_cycles())):
    s,l,p=spectrum(palindromes_via_windows(word))
    rows.append((word,s,l,p)); joint[s,l]+=1;prof[p]+=1
out=Path(__file__).resolve().parent
(out/'joint_spectrum.tsv').write_text('total\tlongest\tcycles\n'+'\n'.join(f'{s}\t{l}\t{n}' for (s,l),n in sorted(joint.items()))+'\n',encoding='utf-8')
(out/'lengthwise_profiles.tsv').write_text('profile_lengths_1_to_32\tcycles\n'+'\n'.join(','.join(map(str,p))+'\t'+str(n) for p,n in sorted(prof.items()))+'\n',encoding='utf-8')
(out/'full_census.tsv').write_text('cycle_bits\ttotal_distinct\tlongest\tprofile_lengths_1_to_32\n'+'\n'.join(w+'\t'+str(s)+'\t'+str(l)+'\t'+','.join(map(str,p)) for w,s,l,p in rows)+'\n',encoding='utf-8')
print('rows',len(rows),'joint',len(joint),'profiles',len(prof))
