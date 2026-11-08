# Independent mathematical audit

## correctness

PASS

Let S=(2,2,2) smooth K3 in P5 containing a line E, H²=8,H.E=1,E²=-2, D=2H+E, C~mD smooth connected and disjoint E. Ambient S arithmetically Cohen–Macaulay gives H1(I_C(t))=H1(S,O((t-2m)H-mE)). For t<2m, Serre duality makes this h1(kH+mE), k=2m-t>0. Exact E-filtration with restriction O_E(k-2j), Kodaira vanishing of kH and h2=0, yields sum_{j=1}^m max(0,2j-k-1)=0 if t<=1, floor(t²/4) for 2<=t<=2m-1. At t=2m, mE rigid with h0=1,h2=0 and Riemann–Roch chi=2-m² gives h1=m²-1, not floor((2m)²/4). Adjunction and E|C trivial imply O_C(mH)^2=K_C; h0(C,mH)=4m²+2+floor(m²/4), odd exactly m=2 mod4. Reconstructed recurrence for m=1..20 and all t=-2..2m; checked sample m2/m3 and original verify_rao.py up to m64. These finite tests corroborate the unrestricted exact-sequence proof and not an independent geometric existence proof.

## originality

PASS

Best-of-knowledge comparison against stronger and equivalent claims, not titles alone; primary texts and known antecedents acknowledged. The all-twist and spin counts require an explicit recurrence on O_E(k-2j) and Riemann–Roch endpoint. Those standard tools, together with family parameters, reconstruct claim, but earlier printed conclusions do not directly state it. Unresolved historical-priority possibilities are explicitly retained; unsuccessful searches are not proof of novelty.

## value

PASS

For the natural ample-embedding K3 curve family with exceptional contracted line and nontrivial embedded deficiency, the complete pre-canonical graded Hartshorne–Rao profile and induced theta-characteristic parity distinguish the exceptional endpoint and offer precise inputs for Hilbert/deformation and spin studies. The claim is specifically an explicit family-wide classification, not a new K3 vanishing theorem or full module multiplication structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
