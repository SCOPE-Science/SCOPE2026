# A single corner feedback bit creates maximal-length cycles on rectangular parity grids

## Finding

For each integer \(b\ge3\), let \(n=2^b-1\) and consider the \(3\times n\) rectangular grid with zero exterior boundary. On every vertex, synchronous states in a finite field \(\mathbb F_q\) of characteristic two evolve by summing the four available orthogonal neighbor states. Let \(A_b\) be this linear map, let \(e\) be the upper-left corner basis vector, and change only that vertex by also summing its own previous state: \(B_b=A_b+ee^{\mathsf T}\).

The unperturbed map \(A_b\) is nilpotent. In contrast,
\[
\det(zI-B_b)=z^{2n}p_b(z),\qquad
p_b(z)=z^{2^b-1}+z^{2^b-2}+\sum_{j=3}^{b}z^{2^b-2^j}.
\]
The polynomial \(p_b\) is squarefree and has nonzero constant term. Consequently, the recurrent (periodic) subspace has dimension exactly \(n\), and **exactly \(q^n\) of the \(q^{3n}\) states are periodic**. More precisely, for any positive integer \(t\),
\[
\#\operatorname{Fix}(B_b^t)=q^{\deg\gcd(p_b(z),z^t-1)}.
\]
For \(b\) odd, zero is the sole fixed configuration; for \(b\) even there are exactly \(q\) fixed configurations. Möbius inversion of these fixed-point counts gives every primitive-period population.

For binary states and \(b=3\) (a \(3\times7\) grid), the nonzero periodic subspace is one cycle of least period \(127\). For binary states and \(b=5\) (a \(3\times31\) grid), the nonzero periodic subspace is **one cycle of least period \(2^{31}-1=2147483647\)**. Under a uniformly random binary initial configuration of the latter 93-vertex system, the probability of eventual entry into this long cycle is exactly \(1-2^{-31}\). Without the corner modification, every configuration instead reaches zero.

## Assumptions and scope

Rows and columns are labelled \((i,j)\) for \(0\le i<3\), \(0\le j<n\). Any neighbor outside this rectangle contributes zero; **there are no wrapped or periodic spatial boundaries**. All updates occur simultaneously. At the corner \((0,0)\) only, the previous corner state is included in addition to its existing neighbors. The result applies to every finite field of order \(q=2^h\), \(h\ge1\), except that the assertions about a *single* nonzero primitive cycle explicitly take \(q=2\). The first-entry time for nonperiodic configurations is not specified by the characteristic-polynomial identity.

## Proof

**1. The unperturbed grid is nilpotent.** Let \(T_s\) be the adjacency matrix of the path on \(s\) vertices over characteristic two. The continuants \(f_s(z)=\det(zI-T_s)\) satisfy \(f_0=1\), \(f_1=z\), and \(f_s=zf_{s-1}+f_{s-2}\). In characteristic two the elementary path identities are
\[
f_{2k+1}=z f_k^2,\qquad f_{2k}=f_k^2+f_{k-1}^2.
\]
Induction gives
\[
f_{2^b-1}(z)=z^{2^b-1},\qquad f_{2^b-2}(z)=\sum_{j=1}^{b}z^{2^b-2^j}.
\]
Thus \(T_n\) and \(T_3\) are nilpotent by Cayley–Hamilton. The grid matrix is \(A_b=T_3\otimes I_n+I_3\otimes T_n\), so, using the characteristic-two Frobenius rule,
\[
A_b^{2^b}=T_3^{2^b}\otimes I_n+I_3\otimes T_n^{2^b}=0.
\]
In particular \(\det(zI-A_b)=z^{3n}\).

**2. The corner-return moments.** For a path, Cramer's rule gives the corner resolvent \(((zI-T_s)^{-1})_{00}=f_{s-1}(z)/f_s(z)\). The Laurent series for \(T_n\) therefore has nonzero corner-return moment precisely at times \(2^j-2\) for \(1\le j\le b\), and the path of length three has corner-return moments at times zero and two. Writing \(u_t=(T_n^t)_{00}\), \(v_t=(A_b^t)_{(0,0),(0,0)}\), and taking \(u_t=0\) for \(t<0\), the tensor binomial theorem gives
\[
v_t=u_t+\binom{t}{2}u_{t-2}\quad\text{in characteristic two}.
\]
The second binary digit of \(t\) controls \(\binom{t}{2}\bmod2\). Directly from the explicit support of \(u_t\),
\[
v_t=1\quad\Longleftrightarrow\quad t=0\ \text{or}\ t=2^j-2\ \text{for some }3\le j\le b;
\]
all other corner-return moments vanish. This is an identity for every nonnegative integer \(t\), since \(A_b\) is nilpotent.

**3. The rank-one feedback characteristic polynomial.** The matrix determinant lemma over \(\mathbb F_q(z)\), where subtraction agrees with addition, yields
\[
\det(zI-B_b)=z^{3n}\left(1+\sum_{t\ge0}v_tz^{-t-1}\right).
\]
Substituting the support of \(v_t\), and using \(n=2^b-1\), gives exactly \(z^{2n}p_b(z)\) as claimed. Its constant term is one (the summand \(j=b\)). Its formal derivative is \(p_b'(z)=z^{n-1}\), since \(n\) is odd and all other positive exponents are even. Therefore \(\gcd(p_b,p_b')=1\): the polynomial is squarefree.

**4. Periodic-state census.** The primary decomposition of the finite-dimensional map \(B_b\) splits the state space into a \(2n\)-dimensional nilpotent sector and an \(n\)-dimensional invertible sector. A state is periodic exactly when its nilpotent projection vanishes, so there are \(q^n\) periodic states. Because \(p_b\) is squarefree, the restriction to the invertible sector has minimal and characteristic polynomial both equal to \(p_b\), and is similar to its companion matrix. The kernel of \(B_b^t-I\) on this sector has dimension \(\deg\gcd(p_b,z^t-1)\), proving the fixed-iterate formula. Evaluating \(p_b(1)\) gives \(b\bmod2\) because \(p_b\) contains exactly \(b\) monomials; squarefreeness makes the eigenvalue-one eigenspace exactly one-dimensional when \(b\) is even and zero otherwise.

**5. The maximal-length special cases.** For \(b=3\), \(p_3(z)=z^7+z^6+1\); for \(b=5\), \(p_5(z)=z^{31}+z^{30}+z^{24}+z^{16}+1\). Exact binary polynomial arithmetic gives, for each degree \(d\in\{7,31\}\), \(z^{2^d}\equiv z\pmod{p_b}\), and \(\gcd(p_b,z^2-z)=1\). Both \(d\) are primes, so Rabin's criterion shows these two polynomials are irreducible. Elementary trial division verifies that \(2^7-1\) and \(2^{31}-1\) are primes. Since the multiplicative group of \(\mathbb F_{2^d}\) has prime order \(2^d-1\), every nonzero element except the identity has that order; the irreducible root cannot be the identity because its minimal polynomial has degree \(d>1\). By the companion-matrix description, all nonzero recurrent binary states form a single orbit of that length. The nilpotent sector is independent of the invertible one, so a uniform binary state enters the nonzero orbit exactly when its invertible projection is nonzero, which has probability \(1-2^{-d}\). This gives the asserted probability when \(d=31\).

## Verification

The accompanying standalone scripts \(verify_matrix.py\), \(verify_orbits.py\), and \(verify_polynomial.py\) were executed with Python's standard library. The first constructs the adjacency matrices independently for the \(3\times7\), \(3\times15\), and \(3\times31\) rectangles and checks all nonzero corner-return moments, the predicted eventual ranks, and extinction without feedback. The second directly evolves the 127 nonzero recurrent configurations on \(3\times7\), checking their period and the seven-dimensional recurrent rank. The third verifies irreducibility over \(\mathbb F_2\) by exact polynomial arithmetic and the primality of the two cycle lengths by complete trial division. See \(verification_output.txt\) for their captured output. These finite checks corroborate the algebraic infinite-family proof; they do not themselves establish its universal quantifiers.

## Relationship to prior work

Martin, Odlyzko and Wolfram (1984), especially Sections 4D and 4F, develop algebraic methods for additive cellular automata, including multidimensional and boundary-condition variants. Their inspected treatments use spatially homogeneous rules and do not present this specific single-corner feedback characteristic polynomial, the all-parameter recurrent census, or the 93-cell primitive cycle. Ciandrini and collaborators (2008) study XOR dynamics and feedback on random directed networks, without the present exact zero-boundary rectangular calculation. Temiz, Sah and Akın (2019) address finite two-dimensional hybrid automata with rank and reversibility results for different diamond/cross-rule families; their paper does not state this single-corner von Neumann feedback cycle census. An earlier square-grid corner-feedback calculation concerns \((2^a-1)\times(2^a-1)\) grids and yields a one-dimensional periodic sector; it does not imply the rectangular \(3\times(2^b-1)\) result for \(b\ge3\).

## Limitations

The general characteristic-polynomial result is confined to width three and the special lengths \(2^b-1\), with only one corner modified and characteristic-two state fields. No all-size maximal period law is claimed: the primitive one-cycle statements are proved at \(b=3\) and \(b=5\), not for every \(b\). Periodicity counts do not determine the complete nonperiodic first-entry distribution. Literature searching cannot rule out uncatalogued equivalent treatments of hybrid two-dimensional automata.

## References

1. O. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258. DOI: 10.1007/BF01223745. Open full text: https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf .
2. L. Ciandrini, C. Maffi, A. Motta, B. Bassetti and M. Cosentino Lagomarsino, *Feedback topology and XOR-dynamics in Boolean networks with varying input structure*, arXiv:0809.1526 (first posted 2008-09-09), subsequently Physical Review E 80 (2009), 026122.
3. F. Temiz, F. Sah and H. Akın, *Reversibility of a Family of 2D Cellular Automata Hybridized by Diamond and Cross Rules Over Finite Fields and an Application to Visual Cryptography*, Journal of Cellular Automata **14** (2019), 241–262.
