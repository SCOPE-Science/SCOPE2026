# Dihedral Case-2 verdict for the symmetric 1/3 Heun operator at t = -1

## Context

Consider the Heun equation

y'' + (gamma/z + delta/(z-1) + epsilon/(z-t)) y'
  + (alpha*beta*z - q)/(z(z-1)(z-t)) y = 0

at t=-1, gamma=delta=epsilon=2/3, alpha=1/3, beta=2/3, q=0. The target asks whether this point lies in the imprimitive/dihedral Kovacic case and, more generally, whether it has Liouvillian solutions.

For a second-order equation with a first-derivative term, Kovacic's algorithm is applied after passing to the normal form. That algebraic normalization must be kept distinct from the Picard-Vessiot group of the original equation over C(z).

## Definitions

Put

P = (2/3)(1/z + 1/(z-1) + 1/(z+1)),
Q = (2/9)/(z^2-1),
D = z(z^2-1).

Let a=D^(1/3), so a'/a=P/2, and set xi=a y. Then xi satisfies the SL-form equation

xi'' = r xi,

where r=P^2/4+P'/2-Q belongs to C(z).

## Result

The normalized equation xi''=r xi has differential Galois group SL_2(C). Kovacic Cases 1, 2, and 3 all fail, so it has no Liouvillian solution; in particular the projective equation is not in the infinite-dihedral case.

For the original Heun equation over C(z), the full Picard-Vessiot group is not literally SL_2(C). It is

mu_3 · SL_2(C) = { g in GL_2(C) : det(g)^3 = 1 },

with identity component SL_2(C). Thus the original equation is likewise non-Liouvillian and non-dihedral, while its finite determinant character records the cubic algebraic normalization.

## Proof / evidence

Exact rational simplification gives

r = -2(z^2+1)^2 / (9 z^2 (z^2-1)^2).

At z=0,1,-1 and infinity, r has a double pole with coefficient b=-2/9, so sqrt(1+4b)=1/3.

**Kovacic Case 1.** At each singular point the two alpha values are {1/3,2/3}. Every candidate degree

d = alpha_infinity - alpha_0 - alpha_1 - alpha_{-1}

is negative; its maximum is 2/3-3(1/3)=-1/3.

**Kovacic Case 2.** The integer set at every singular point is E={2}. The unique degree is

d=(2-2-2-2)/2=-2,

so Case 2 is impossible.

**Kovacic Case 3.** For n=4,6,12 the relevant integer sets are respectively {4,5,6,7,8}, {4,6,8}, and {4,5,6,7,8}. Even in the extremal choice,

e_infinity - e_0 - e_1 - e_{-1} <= 8-12=-4,

so every candidate degree is negative. Therefore all three Liouvillian cases fail and the normal-form Galois group is SL_2(C).

It remains to recover the group of the original equation. Let K=C(z), let L be the Picard-Vessiot field of the normalized equation, and let a^3=D. Since Gal(L/K)=SL_2(C) is connected, K is algebraically closed in L; hence the cyclic cubic extension K(a)/K is linearly disjoint from L/K. The Wronskian W_y of the original equation satisfies

W_y'=-P W_y,

so W_y is a nonzero constant multiple of D^(-2/3)=a^(-2). Therefore the original Picard-Vessiot field M contains a (because a=D a^(-2)), and then xi=a y shows that M also contains L. Conversely y=xi/a shows M is contained in L(a), hence M=L(a).

Thus Gal(M/K) is SL_2(C) x mu_3 abstractly. On the original y-solution space, (g,zeta) acts as zeta^(-1)g. Its image is exactly mu_3·SL_2(C), equivalently the subgroup of GL_2(C) whose determinant has cube one.

## Limitations

The verdict is specific to the single point t=-1, gamma=delta=epsilon=2/3, alpha=1/3, beta=2/3, q=0. It does not classify nearby accessory parameters or other Heun families. The archived script checks the exact normalized Kovacic calculation; the finite cubic determinant extension of the original equation is established by the Wronskian and field argument above. Arithmetic monodromy is not addressed.

## Reproducibility

Run `python3 artifacts/kovacic_verdict.py` with SymPy. It checks the exact normal-form coefficient, all double-pole data, and the negative-degree obstructions in Kovacic Cases 1-3.

## References

- J. J. Kovacic, *An algorithm for solving second order linear homogeneous differential equations*, J. Symbolic Comput. 2 (1986), 3-43, doi:10.1016/S0747-7171(86)80010-4.
- M. van der Put and M. F. Singer, *Galois Theory of Linear Differential Equations*, Springer, 2003.
- DLMF Chapter 31, especially §§31.8 and 31.14.
