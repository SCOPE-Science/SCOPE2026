# Independent mathematical audit

## correctness

PASS

Both rules elect the unique largest approval support in round one. With first winner C and support d, an eligible second candidate with s>0 approvals and u supporters outside C has doubled PAV marginal s+u and Phragmen load 1/d+(d-u)/(ds). The common load is feasible without lowering anyone's existing load because u<=s<d. A zero-approval candidate cannot be a unique second winner in a strict disagreement. Naming A the Phragmen choice and B the PAV choice gives b+q>a+p and a(d-q)>b(d-p). For t=a-b=0 these conflict. If t>0, q>=p+t+1 and a>=p+2t+1, while dt>a(q-p)+tp. For t=1 these force n>=9+4p, with n=9 allowing only d,a,b,p,q=7,3,2,0,2. For t>=2 they force d>=2t+4 and n>=3t+5. If t<0, h=b-a and r=p-q must obey 1<=r<=h-1 and b(h-r)<h(p-r-1); this gives p>=3 and n>=2p+h+1>=9. Equality forces p=3, r=1, h=2, a=3, b=5, d=6, for which 9>12 would be required and fails. The only surviving support tuple at nine determines all ballots, with six distinct relabelings. For the representative, PAV scores are 3/2 and 2 and Phragmen loads are 10/21 and 1/2. Extra C-only ballots preserve the PAV comparison and make the Phragmen comparison 3(d-2)>2d, true for every d>=7.

## originality

PASS

Prior two-seat disagreement is explicit in Janson, and one prior example yields the same three-ballot support pattern by restriction to the two differing committees' union. The contribution supported here is the sharp nine-voter minimum, proof of impossibility below it, the complete single-orbit classification at it, and strict witnesses for every size thereafter. The underlying rules, qualitative divergence and support template are not credited as new.

## value

PASS

Three candidates and two seats are the first nontrivial domain: with one seat the rules are both approval voting, and two seats with two candidates choose the whole set. Removing dependence on ties distinguishes real score differences from tie policy. The sharp minimum and the complete extremal orbit supply a precise benchmark for comparing methods with the same first-round behavior but different second-round weighting, beyond an example of divergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
