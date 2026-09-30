# Finite-volume strict semistability of a Kummer pullback on a Goldstein–Prokushkin–Fu–Yau threefold

## Context

The Hull–Strominger system requires, among other equations, a
Hermitian–Yang–Mills (HYM) connection on the gauge bundle. On a
Goldstein–Prokushkin (GP) torus bundle over a K3 surface carrying a
Fu–Yau balanced metric, this record tests a specific pullback of a
strictly semistable rank-2 extension from the Kummer base. The question
here is only whether that pullback can be stable/polystable for the
chosen balanced class and hence serve as an HYM gauge bundle.

## Definitions

Let S=Km(E x E) be a smooth projective Kummer K3 with classes
<h,e_1,...,e_16>, h^2=2, h.e_i=0 and e_i.e_j=-2 delta_ij. Put
D=e_1-e_2, L=O_S(D), F_1=e_3-e_4, F_2=e_5-e_6, and choose N large
enough that H=N h-sum e_i is ample. Let E be a non-split extension

  0 -> L -> E -> L^{-1} -> 0.

Let pi:X->S be a GP holomorphic T^2-bundle whose integral curvature
classes are F_1,F_2, and let omega_u be a Fu–Yau metric built from a
Kähler form omega_S in the class H. Write
tau=||Omega||_{omega_u} omega_u^2 for its balanced (2,2)-form. The
slope is mu_tau(F)=rk(F)^{-1} int_X c_1(F) wedge tau.

## Result

For every finite positive fiber scale in the GP/Fu–Yau ansatz,

  mu_tau(pi^*L)=0=mu_tau(pi^*E).

Therefore pi^*L is an equal-slope line subbundle of pi^*E, so pi^*E is
not stable. The pulled-back extension remains non-split; as an extension
of degree-zero line bundles it is semistable, and its non-splitting means
it is not polystable. By the Hermitian–Einstein/Hermitian–Yang–Mills
correspondence on Gauduchon manifolds, pi^*E admits no HYM metric in
this balanced conformal class. Consequently this particular pullback
cannot be the HYM gauge bundle in a Hull–Strominger solution using this
balanced class. No conclusion about the Green–Schwarz/Bianchi identity
by itself is asserted.

## Proof / Evidence

Base arithmetic: D^2=-4 and H.D=0. On the K3 surface,
chi(L^2)=2+(2D)^2/2=-6. Since 2D is nonzero and has degree zero with
respect to the ample H, neither L^2 nor L^{-2} has a nonzero section;
hence h^1(L^2)=6 and non-split extensions exist. Whitney gives
c_1(E)=0 and c_2(E)=-D^2=4.

Slope: in the standard GP/Fu–Yau ansatz, up to positive normalization
constants the balanced form tau is a sum of a horizontal term
proportional to pi^*(omega_S^2) and a mixed term proportional to
pi^*omega_S wedge i theta wedge bar(theta). Wedge with pi^*D. The
first term is the pullback of a degree-six form on the complex surface S
and therefore vanishes. The mixed term integrates to a positive fiber
constant times int_S D wedge omega_S, which is H.D=0. Fiber rescaling
changes only that positive coefficient, so the slope remains zero at
every finite positive fiber scale. Since c_1(E)=0, mu_tau(pi^*E)=0.
This direct calculation does not require a symmetry argument.

Non-splitting after pullback follows from the Leray five-term sequence.
Because pi_*O_X=O_S for the connected torus fibration, projection formula
gives an injection

  H^1(S,L^2) -> H^1(X,pi^*L^2).

Thus the nonzero extension class remains nonzero. The extension of the
two degree-zero line bundles is semistable; a polystable bundle with the
same Jordan–Hölder factors would split, contradicting the injected
extension class. Hence pi^*E is strictly semistable and non-polystable.
The Gauduchon Kobayashi–Hitchin correspondence then excludes an HYM
metric.

The arithmetic and finite-scale zero-slope identity are reproduced by
artifacts/slope_check.py.

## Limitations

The claim is for the stated GP torus bundle and Fu–Yau balanced ansatz
with base class H. It does not address other balanced classes, other line
bundles, deformations that change H.D, or adiabatic limiting questions.
It makes no independent claim that the Bianchi/Green–Schwarz equation
fails. The earlier draft's expression 2||gamma||^2 for a smooth splitting
endomorphism is not called a string-algebroid Futaki invariant: the
Futaki construction in the cited work is defined for holomorphic anchored
endomorphisms, while the diagonal splitting endomorphism of a non-split
extension is not holomorphic.

## Reproducibility

Run `python3 artifacts/slope_check.py`; it checks D^2=-4, H.D=0,
chi(L^2)=-6, h^1=6, c_2(E)=4, and the zero slope at several positive
fiber scales. The script deliberately does not certify ampleness for a
specific numerical N; ampleness is an input chosen with N sufficiently
large.

## References

Fu–Yau, the superstring with flux / Fu–Yau equation papers;
Goldstein–Prokushkin on non-Kähler Calabi–Yau torus bundles;
Li–Yau on Hermitian–Yang–Mills connections on non-Kähler manifolds;
M. Garcia-Fernandez and R. Gonzalez Molina, Futaki Invariants and Yau's
Conjecture on the Hull-Strominger system, arXiv:2303.05274.
