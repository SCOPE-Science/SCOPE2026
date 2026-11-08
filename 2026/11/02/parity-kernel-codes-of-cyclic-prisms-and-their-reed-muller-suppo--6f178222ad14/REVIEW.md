# Independent mathematical audit

## correctness

PASS

Upper closed-neighborhood parity yields b_i=a_(i-1)+a_i+a_(i+1) over F2; substituting into lower equation gives a_(i+4)=a_i, with converse verified. The 4-periodic and n-periodic sequence has exactly gcd(n,4) independent bits. For g=4, the 8 coordinate linear forms of one 4-rung prism are exactly the odd Hamming-weight vectors of F2^4, an affine 3-flat, so this code is precisely RM(1,3) up to permutation; g=1 and g=2 follow directly. Zero/nonconstant/one affine function weights and maximally compatible common zero sets give enumerator and generalized Hamming weights. Symmetric closed-neighborhood matrix rank/nullity gives 2^(-g) Lights-Out target fraction. Fresh independent parity nullspace and word census n=3..32, plus subcode support minima for all g=4 cases, passed. Original verify.py code was inspected; no finite test was used as infinite proof.

## originality

PASS

Qualified PASS for the complete cyclic-prism parity-code classification and generalized weights. Existing nullspace/dominating-set papers establish the parity model mostly for open rectangular grids; standard RM facts determine weights once an equivalence is proved. The four-step prism recurrence and code equivalence were not found stated as a combined theorem. Older cylinder Lights-Out literature remains a meaningful priority risk.

## value

PASS

PASS. The closed-neighborhood kernel is a natural Lights-Out invariant and its full code rather than mere dimension determines quiet configurations, weights and support-reachability; a complete cyclic-family identification with RM(1,3) is a motivated reusable classification even though derivation is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
