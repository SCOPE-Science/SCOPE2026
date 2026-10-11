# Morse energy forces an index-one branched minimal fiber
## Finding
Let \(S\) be a closed oriented surface of genus \(g\ge 2\), let \(f:S\to S\) be an orientation-preserving pseudo-Anosov homeomorphism, and let
\[
M_f=S\times[0,1]/(x,1)\sim(f(x),0)
\]
be its closed hyperbolic mapping torus. For each marked conformal structure \(X\in\mathcal T(S)\), let \(h_X:(S,X)\to M_f\) be the unique harmonic map freely homotopic to the fiber inclusion, and write \(\mathcal E(X)\) for its energy.

The monodromy invariance of \(\mathcal E\) gives a descended proper function
\[
\overline{\mathcal E}:\mathcal T(S)/\langle f\rangle\longrightarrow\mathbb R.
\]
Assume that \(\overline{\mathcal E}\) is a Morse function. Then \(\overline{\mathcal E}\) has a critical point of Morse index \(1\). Hence there is a \(\langle f\rangle\)-orbit of conformal structures \(X\) such that \(h_X\) is a branched minimal immersion homotopic to the fiber and
\[
\mathcal E(X)>A_0,
\]
where \(A_0\) is the least area among maps homotopic to the fiber. In particular, this orbit is distinct from every least-area-fiber orbit. Thus the Morse hypothesis forces at least two critical orbits of the harmonic energy: a global-minimum orbit of index \(0\) and a non-minimizing orbit of index \(1\).

## Assumptions and scope
The target is the closed hyperbolic mapping torus of a pseudo-Anosov homeomorphism of a closed oriented surface of genus at least \(2\). The harmonic energy is exactly the function studied by Verjovsky. The additional hypothesis is that its descended function on the cyclic Teichmüller quotient is Morse, meaning that every critical point is nondegenerate.

No genericity statement for this Morse hypothesis is claimed. The result is conditional: it identifies a forced critical orbit if nondegeneracy holds for the unperturbed descended energy attached to the given mapping torus.

## Proof
Verjovsky proves that the harmonic representative \(h_X\) exists uniquely for every \(X\), that
\[
d\mathcal E_X(\mu)=-4\operatorname{Re}\int_X\Phi_X\mu,
\]
where \(\Phi_X\) is the Hopf differential, and therefore
\[
d\mathcal E_X=0\quad\Longleftrightarrow\quad\Phi_X=0.
\]
The same paper proves monodromy invariance \(\mathcal E(f^*X)=\mathcal E(X)\) and, using Goldman--Wentworth, properness of the descended function \(\overline{\mathcal E}\) on the cyclic quotient.

A pseudo-Anosov mapping class has infinite order and no fixed point in Teichmüller space; its cyclic action is properly discontinuous. Since \(\mathcal T(S)\) is contractible, the quotient
\[
Q=\mathcal T(S)/\langle f\rangle
\]
has universal cover \(\mathcal T(S)\) and fundamental group \(\mathbb Z\). Hence \(Q\) is a \(K(\mathbb Z,1)\), and for every field \(\mathbb F\),
\[
H_1(Q;\mathbb F)\cong\mathbb F.
\]

Now assume \(\overline{\mathcal E}\) is Morse. It is proper and bounded below, so its compact sublevel sets give a Morse exhaustion of \(Q\). The Morse chain complex over \(\mathbb F\) computes \(H_*(Q;\mathbb F)\). Because \(H_1(Q;\mathbb F)\ne0\), the degree-one Morse chain group cannot vanish. Therefore \(\overline{\mathcal E}\) has at least one critical point of Morse index \(1\).

Lift such a point to \(X\in\mathcal T(S)\). The quotient map is locally a diffeomorphism, so \(X\) is a critical point of \(\mathcal E\). Thus \(\Phi_X=0\), and \(h_X\) is weakly conformal and harmonic. It is nonconstant because it lies in the fiber homotopy class, whose induced surface-group map is injective. Hence \(h_X\) is a branched minimal immersion.

An index-one critical point cannot be a global minimum. Verjovsky proves
\[
\min\mathcal E=A_0
\]
and characterizes equality by least-area maps, which are conformal embeddings onto least-area fibers. Therefore the index-one orbit satisfies \(\mathcal E(X)>A_0\) and is not represented by a least-area fiber. A global minimum exists and has index \(0\) under the Morse hypothesis, so the two critical orbits are distinct.

## Verification
The argument is formal and does not rely on finite experimentation. The critical source statements were checked in the open full text: the critical-point/Hopf-differential equivalence, monodromy invariance, properness on the cyclic quotient, the description of global minima, and the free properly discontinuous pseudo-Anosov orbit. The only additional input is the standard weak Morse inequality on a proper Morse exhaustion.

As a boundary check, the conclusion is not asserted without the Morse hypothesis. Degenerate critical loci can carry topology that is invisible to the count of isolated Morse critical points, so the index-one conclusion cannot be obtained from \(H_1(Q)\ne0\) by the same argument in the degenerate case.

## Relationship to prior work
Verjovsky identifies critical points of \(\mathcal E\) with zeros of the Hopf differential, proves monodromy invariance, imports properness of the descended energy from Goldman--Wentworth, and identifies the global minima with least-area fibers. The inspected paper does not apply Morse inequalities to the cyclic quotient and contains no statement forcing an index-one critical orbit or a non-minimizing branched minimal immersion.

Goldman--Wentworth prove properness of the twisted harmonic-map energy on the quotient by the group induced from a normal-subgroup extension; their motivating example is precisely a fibered hyperbolic \(3\)-manifold with cyclic monodromy quotient. Their inspected text does not state the index-one consequence or a critical-point multiplicity theorem for this cyclic quotient.

The new step is topological: because the quotient is a \(K(\mathbb Z,1)\), its nonzero first homology forces an index-one generator in the Morse complex whenever the descended energy itself is Morse. This converts the recent variational framework into a forced non-minimizing branched minimal fiber.

## Limitations
The result does not prove that \(\overline{\mathcal E}\) is Morse for any particular mapping torus, nor that the index-one branched minimal immersion is embedded. It gives no quantitative estimate for its energy above \(A_0\), its area, or its branch set.

Originality checks covered the recent primary full text, Goldman--Wentworth's properness paper, targeted searches for Morse, index-one, non-minimizing, and branched-minimal formulations, a semantic research index, and the available current and prior owned records. An unindexed observation making the same Morse-theoretic deduction remains a residual risk.

## References
1. A. Verjovsky, *Cannon--Thurston Maps, Harmonic Maps, and Minimal Surfaces in Fibered Hyperbolic 3--Manifolds*, arXiv:2609.35858v1, first posted 2026-09-25.
2. W. M. Goldman and R. A. Wentworth, *Energy of Twisted Harmonic Maps of Riemann Surfaces*, arXiv:math/0506212; Contemporary Mathematics 432 (2007).
3. J. Milnor, *Morse Theory*, Annals of Mathematics Studies 51, Princeton University Press, 1963.
