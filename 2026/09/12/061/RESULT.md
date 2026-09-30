# One-pointed psi^5 point descendant on F1 in class 3H-2E

Let X=F1=Bl_p P^2, write E for the exceptional curve and F=H-E for a fibre, and let beta=3H-2E=3F+E. Then c1(X).beta=7, so vdim_C Mbar_{0,1}(X,beta)=7. The insertion psi^5·pt also has codimension 7.

Using the standard toric divisors D1=F, D2=E, D3=F, D4=H, their pairings with beta are

(D1.beta,D2.beta,D3.beta,D4.beta)=(1,2,1,3).

For the Fano toric I-function the beta coefficient is

I_beta = z Q^beta / [(D1+z)(D2+z)(D2+2z)(D3+z)(D4+z)(D4+2z)(D4+3z)].

Its leading scalar term is

Q^beta · z^{-6}/(1!2!1!3!) = Q^beta · z^{-6}/12.

In the standard one-point J-function, the coefficient of the identity class at z^{-6} is dual to a point insertion and equals <tau_5(pt)>_{0,1,beta}. Hence

<tau_5(pt)>_{0,1,3H-2E}^{F1} = 1/12.

The only c1=1 Mori generator is E. Its toric pairing vector contains a -1 entry, so its I-term begins at order z^{-1}; it does not create a z^0 mirror-map correction. Thus the displayed coefficient is not altered by a change of variables.

## Reproducibility and limitations

The factorial and grading calculation above was independently recomputed in the 2026-09-29 audit. The previously referenced `output/artifacts/leading_coeff.py` is not present in the audited repository tree and is not claimed as evidence. The derivation relies on the published toric mirror theorem and standard small-J conventions.

## References

- Coates, Corti, Iritani, Tseng, *A Mirror Theorem for Toric Stacks*, arXiv:1310.4163.
- Cooper, *A Fock Space approach to Severi Degrees of Hirzebruch Surfaces*, arXiv:1709.01159, for broader curve-counting context on Hirzebruch surfaces.
