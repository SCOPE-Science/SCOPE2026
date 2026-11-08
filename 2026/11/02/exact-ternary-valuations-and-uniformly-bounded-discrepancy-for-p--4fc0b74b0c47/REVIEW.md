# Independent mathematical audit

## correctness

PASS

Verified companion matrix M has characteristic polynomial x^3-x-1 and exact return M^13=I+3A with A matrix [[2,3,4],[4,5,7],[3,4,5]]. Direct matrix products give unit 3-adic trace slopes at r=1,3,9: 17,29,158. For h with valuation s, nonlinear binomial terms of (I+3A)^h have 3-adic order >=s+2, hence each F_r(m)=R(13m+r)/3 has exact isometric differences and a unique 3-adic zero βr. Regular mod13 branches and r=0 yield the valuation law. Count three root-class residue progressions for pt>=2 and the nine unit classes/other branches, giving p0=9/13,p1=3/13,pt=6/(13*3^t) and discrepancy <=9 from at most nine arithmetic progressions. Independently checked matrix, slopes and 30000 finite indices, and examined VERIFY.py root-lifting/congruence code; finite tests not proof of unbounded statement.

## originality

PASS

The same unshifted Perrin sequence is classical and prime-2 valuation formulae are earlier work. Rihane–Togbé 2021 uses a known 2-adic lemma; Bravo–Irmak analyzes shifted Padovan/Perrin 2-adic valuations. OEIS A001608 supplies sequence values, not the all-index prime-three 13-step root isometry and bounded-discrepancy distribution. Similar p-adic recurrence techniques are acknowledged; no equivalent full theorem located in checked primary statements.

## value

PASS

Exact 3-adic valuation stratification for a classical recurrence naturally complements known 2-adic results. The 13-step return and three root branches yield full frequency distribution and a strong cutoff- and level-uniform discrepancy bound, a useful global arithmetic invariant rather than mere tabulation of initial terms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
