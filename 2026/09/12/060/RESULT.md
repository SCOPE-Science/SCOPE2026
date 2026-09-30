# Exact genus-zero one-pointed descendant on toric dP3

Let X be the blow-up of P^2 at its three torus-fixed points, with H the pullback of a line and E1,E2,E3 the exceptional classes. Put beta=4H-2E1-E2-E3. For the six toric prime divisors
D1=E1, D2=H-E1-E3, D3=E3, D4=H-E2-E3, D5=E2, D6=H-E1-E2,
the pairings with beta are (2,1,1,2,1,1), and c1(X).beta=8.

The one-point invariant <tau_7(H)> has the correct virtual codimension: vdim_C Mbar_{0,1}(X,beta)=8 and psi^7 H has codimension 8.

For a smooth toric Fano surface, the small toric I-function lies on the Givental cone and, in this case, has the trivial divisor mirror map. The beta coefficient is

I_beta = z Q^beta / prod_i prod_{m=1}^{D_i.beta}(D_i+m z).

Since prod_i (D_i.beta)! = 4,

I_beta = Q^beta [ (1/4) z^{-7} - (1/4) S z^{-8} + O(z^{-9}) ],

where S=sum_i H_{D_i.beta} D_i. Direct substitution gives

S = (7/2)H - (1/2)E1 - (3/2)E2 - (3/2)E3.

Therefore the coefficient of H z^{-8} is -(1/4)(7/2)=-7/8. In the standard one-point J-function expansion this coefficient is exactly <tau_7(H)>_{0,1,beta}, because H is self-dual for the intersection pairing against the chosen divisor basis. Thus

<tau_7(H)>_{0,1,4H-2E1-E2-E3} = -7/8.

The possible c1=1 effective toric classes do not create a z^0 mirror-map correction: each has a negative self-pairing with one toric divisor, so its I-term starts at order z^{-1}. Hence no lower-degree mirror substitution changes the displayed coefficient.

## Reproducibility and limitations

The arithmetic above is self-contained and was independently recomputed in the 2026-09-29 audit. The previously referenced files `output/artifacts/mirror_check.py` and `output/artifacts/verify_all.py` are not present in the audited repository tree and are therefore not claimed as reproducibility evidence. The derivation relies on the published toric mirror theorem and standard J-function conventions.

## References

- Coates, Corti, Iritani, Tseng, *A Mirror Theorem for Toric Stacks*, arXiv:1310.4163.
- Iritani, *Shift operators and toric mirror theorem*, Geometry & Topology 21 (2017), 315-343.
- Mandel, Ruddat, *Descendant log Gromov-Witten invariants for toric varieties and tropical curves*, arXiv:1612.02402.
