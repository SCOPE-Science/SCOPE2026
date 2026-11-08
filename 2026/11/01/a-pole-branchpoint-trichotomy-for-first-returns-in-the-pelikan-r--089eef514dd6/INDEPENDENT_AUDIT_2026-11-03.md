# Independent mathematical audit

## correctness

PASS

Inspected all seven actual blobs (RESULT.md proof, SLOGAN, AUDIT, REVIEW, METADATA, VERIFICATION, verify.py) at the assigned frozen Git tree. For the Lebesgue-conditioned top cell A=[1/2,1), the dyadic zero-prefix level L is a nearest-neighbor walk until first hit of level zero: q moves up, p moves down. Doubling from L=0 reinjects with geometric law Pr(L=j)=2^-j-1; halving moves to level one. The bounded first-passage PGF h_j(z)=r(z)^j with r=z(p+q r²), r=(1-sqrt(1-4pqz²))/(2qz), gives R(z)=z[q r+p/(2-r)] exactly. On the principal branch r(rho)=a=sqrt(p/q), rho=(2sqrt(pq))^-1; for p<4/5 a<2, so neither branchpoint coincides with a pole: local singular coefficients at ±rho yield n^-3/2 rho^-n(c_++(-1)^n c_-) with c_± exactly as in the theorem and 0<c_-<c_+. At p=4/5 the positive root equals 2, yielding R(z)~(2sqrt2)^-1(1-z/rho)^-1/2 and (4/5)^n/(2sqrt(2pi n)). For p>4/5 only, z0=2/(p+4q)<rho is a true pole on the smaller-root sheet (the algebraic candidate z0 for p<4/5 belongs to the other sheet); derivative r'(z0)=(p+4q)^2/(p-4q) gives residue K=p(p-4q)/(p+4q)^2, no competing same-modulus singularity. At p=1 direct R=z/(2-z) gives 2^-n, and at p=1/2 R(1)=1 with sqrt singularity, tail ~sqrt(2/(pi n)); for p<1/2 R(1)=p(3-4p)/(2-3p), so defect and mean boundaries are consistent. Finite exact rational independent walk vs PGF comparison for p=1/3,1/2,3/5,4/5,9/10,1 and all n≤24 agreed, with critical symbolic limit sqrt2/4 and high-n coefficient ratios corroborating the three regimes. Infinite proof comes from explicit PGF and complex singularity transfer, not finite tests; asymptotics are fixed-p, not uniform in p.

## originality

PASS

Qualified best-knowledge PASS ONLY for the explicit, sharp FIRST-RETURN coefficient trichotomy and parity constants, not for the dyadic reset walk, exact first-return PGF, p=4/5 in another observable, or generic singularity transfer. Both Monthus B38 and especially Brevitt–Klages eq 24 (epsilon=0) already provide the exact generating function. Independently compared their claims: Monthus B37/B42 state incorrect uniform branchpoint asymptotic above 4/5; Brevitt–Klages analyze G_00 and QSDs, not the full coefficient asymptotics of F_00. The nontrivial pole vs branchpoint sheet switch and parity-preserving transfer yield the explicitly new corrected statement. Direct prior transformations are the decisive, frankly recorded priority/proximity risk; neither an unsuccessful search nor unpublished formula alone proves novelty.

## value

PASS

The top dyadic cell is a canonical natural recurrence set for the Pelikan doubling/halving process, and return-mass tails are a standard exact statistic needed to quantify excursion lengths. The result corrects a substantive all-p>1/2 n^-3/2 absorption-tail extrapolation in Monthus 2025 (Appendix B) and determines an otherwise unstated 4/5 mechanism change: parity-sensitive n^-3/2 below, inverse-square-root n^-1/2 at collision, and a pole-controlled pure exponential above, including exact constants and a deterministic endpoint. The exponential rate and polynomial prefactor affect long excursions by unbounded factors. This is not a new model or generating function and does not claim broader novelty, but a motivated sharp exact classification that remains useful independently of another downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
