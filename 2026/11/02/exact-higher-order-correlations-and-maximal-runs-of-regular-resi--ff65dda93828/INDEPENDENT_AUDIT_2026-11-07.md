# Independent mathematical audit

## correctness

PASS

For n>=2 and any nonempty finite integer shift set H, the local criterion z regular in Z/p^a iff z is a unit or zero mod p^a is proved: p|z with 0<v_p(z)<a makes z(zy-1) have valuation v_p(z), which cannot vanish mod p^a. Partition starting residues x mod p by whether an occupied shift class c satisfies x+c=0: p-r_p(H) unobstructed classes have p^(a-1) successful lifts, and each occupied class contributes one lift iff all its shifts coincide mod p^a. Chinese remaindering gives the product for C_n(H). For H={0,...,L-1}, exact occupied multiplicities yield the p,p-L and 2p-L piecewise factors, including p and 2p boundary overlaps; nonsquarefree minimal squared-prime q determines maximal length 2q-1 and B_n(2q-1)>0. Double indicator inclusion-exclusion gives exact bounded cyclic run histogram E_n(L)=B_n(L)-2B_n(L+1)+B_n(L+2). Squarefree moduli are explicitly excluded from bounded-run statement. Independent fresh exact-integer residue counting agreed with the product on 714 cases for n=2..120 and six diverse shift sets per modulus. The original verify.py was inspected, not assumed to certify infinity.

## originality

PASS

Best-of-knowledge original extension of regular-integer counting from single residues to exact arbitrary simultaneous shift correlations and a complete run-length histogram. Haukkanen–Toth develop regular-integer Fourier/Ramanujan sums; Dohmen–Lange-Geisler count the regular residues and discuss one-message RSA correctness. Neither inspected theorem states the collision-sensitive local law and its run distribution. A Fourier inversion may give an alternate route but is not itself a demonstrated stronger evaluated formula. Full 2025/1157 and 2026/1589 IACR PDFs were not obtained; only public abstracts were checked, so their priority risk is explicit rather than a scientific FAIL.

## value

PASS

The regular elements of finite residue rings are a natural arithmetic object and their one-point count is classical. Exact multi-translation joint probabilities and full maximal-run distribution measure spatial structure absent from the one-point invariant, with a sharp smallest-squared-prime cutoff and collision-sensitive shifts. Such exact quantities are independently useful for questions about patterns in periodic arithmetic sets; the claim makes no unsupported cryptographic security assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
