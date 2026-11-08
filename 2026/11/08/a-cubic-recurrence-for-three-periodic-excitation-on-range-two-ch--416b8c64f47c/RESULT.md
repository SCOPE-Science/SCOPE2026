# A cubic recurrence for three-periodic excitation on range-two chains

## Finding

For every integer \(n\ge3\), let \(G_n=P_n^2\) denote the square of the \(n\)-vertex path: its labelled vertices are \(1,\ldots,n\) and distinct vertices are adjacent exactly when their indices differ by one or two. Evolve the three-state Greenberg–Hastings automaton synchronously: \(1\mapsto2\), \(2\mapsto0\), while a vertex in state \(0\) moves to \(1\) if and only if it has a neighbor in state \(1\), and otherwise remains \(0\).

Let \(N_n\) be the number of **initial** configurations with least temporal period exactly three, including all temporal phases. Then

\[
N_3=6,\qquad N_4=18,\qquad N_5=42,
\]
\[
N_n=3N_{n-1}-2N_{n-2}+2N_{n-3}\quad(n\ge6),
\]

or equivalently

\[
\sum_{n\ge3}N_n z^{n-3}=\frac{6}{1-3z+2z^2-2z^3}.
\]

The number of distinct primitive three-cycles is \(N_n/3\). If \(\lambda\) is the unique real root of \(x^3-3x^2+2x-2\), then \(\lambda=2.5213797068\ldots\) and \(N_n\sim 6.4174781584\ldots\lambda^{n-3}\). Thus the proportion of all \(3^n\) initial states with primitive temporal period three decays exponentially at rate \((\lambda/3)^n\).

## Assumptions and scope

The graph is a finite **open** range-two chain; there is no wrap-around edge. The result holds for every integer \(n\ge3\), with labelled sites and with all three colors distinguished. The state \(0\) is resting, \(1\) excited, and \(2\) refractory. There is exactly one fixed state, the all-resting configuration, but this result does not classify other eventual periods, attraction basins, or transient lengths. There are no probabilistic assumptions.

## Proof

**Reduction to an exact local phase condition.** Consider any configuration satisfying \(F^3(x)=x\), where \(F\) denotes one synchronous update. Every site initially in state \(1\) or \(2\) necessarily traverses all three states before returning. A site initially in state \(0\) either remains at \(0\) throughout these three updates or traverses \(0\to1\to2\to0\): it cannot turn from \(1\) to \(0\) in one update. An always-resting vertex cannot be adjacent to any cycling vertex, because that neighbor is excited once in each block of three updates. Connectedness of \(G_n\) therefore forces either the all-resting state or every vertex cycling on each update. A fully cycling configuration is primitive period three, since the color at every vertex changes.

For a fully cycling configuration write its initial phase assignment as \(c_i\in\mathbb Z/3\mathbb Z\). At the update when vertex \(i\) has state \(0\), it must have a neighbor in state \(1\). Equivalently,

\[
\text{for every }i,\quad \exists j:\ 1\le j\le n,\ 1\le|i-j|\le2,\quad c_j=c_i+1\pmod 3.
\]

Conversely, this condition guarantees that all vertices advance in each of the next three updates, so the initial configuration is primitive three-periodic. It suffices to count such phase words.

**Finite transfer with open boundaries.** Index an \(81\)-element state set \(\mathcal S=(\mathbb Z/3\mathbb Z)^4\) by ordered tuples \(s=(a,b,c,d)\). Define a left weight \(\ell_s\), terminal weight \(r_s\), and integer transition matrix \(M\) by

\[
\ell_{(a,b,c,d)}=[a+1\in\{b,c\}][b+1\in\{a,c,d\}],
\]
\[
r_{(a,b,c,d)}=[c+1\in\{a,b,d\}][d+1\in\{b,c\}],
\]
\[
M_{(a,b,c,d),(b,c,d,e)}=[c+1\in\{a,b,d,e\}],
\]

with all other entries of \(M\) zero. Brackets are zero-one indicators and every color addition in these expressions is modulo three. The left weight verifies vertices \(1,2\), each transition appends one new vertex and verifies the next middle vertex, and the terminal weight verifies the final two vertices. Consequently,

\[
N_n=\ell^{\mathsf T}M^{n-4}r\qquad(n\ge4).
\]

**Exact cubic transfer identity.** Direct enumeration of the three possible append colors, applied three times to each tuple, gives the finite integer identity

\[
(M^3-3M^2+2M-2I)r=0.
\]

This is an identity of all \(81\) components, **not** a fit to initial terms. It can be checked by hand using only \(27\) cases: simultaneous addition of a constant to every tuple color preserves the definitions, so set \(a=0\). The \(27\) tuples produce just six profiles \((r,Mr,M^2r,M^3r)\):

| \(r\) | \(Mr\) | \(M^2r\) | \(M^3r\) |
| ---: | ---: | ---: | ---: |
| 0 | 0 | 1 | 3 |
| 0 | 1 | 2 | 4 |
| 0 | 1 | 3 | 7 |
| 0 | 0 | 2 | 6 |
| 1 | 1 | 3 | 9 |
| 1 | 2 | 4 | 10 |

For every profile, the fourth entry is three times the third minus twice the second plus twice the first. The complete correspondence between all \(27\) representative tuples and their profiles is printed by the self-contained `verify_transfer.py` certificate. Thus the matrix identity holds for all states and hence, after multiplication by \(\ell^{\mathsf T}M^k\), the claimed recurrence holds for every \(n\ge7\). Exhaustive direct inspection of the short paths gives \(N_3=6\), \(N_4=18\), \(N_5=42\), and \(N_6=102=3N_5-2N_4+2N_3\); this proves the recurrence from \(n=6\) onward. The generating function follows by multiplying the recurrence by powers of \(z\).

**Asymptotics.** The cubic \(x^3-3x^2+2x-2\) has one real positive root \(\lambda=2.5213797068\ldots\) and a complex-conjugate pair of modulus \(\sqrt{2/\lambda}<1\), so \(\lambda\) uniquely dominates the coefficients. At the simple pole \(z_0=1/\lambda\), the dominant partial-fraction coefficient is

\[
C=\frac{6}{3z_0-4z_0^2+6z_0^3}=6.4174781584\ldots,
\]

which gives the asymptotic statement.

## Verification

The standalone script `verify_transfer.py` constructs the complete \(81\)-state matrix implicitly from the preceding definitions, checks every component of the cubic identity over the integers, prints the \(27\) color-translation representatives, and checks the sequence through \(n=40\). It makes no use of numerical fitting or external packages. The independent `verify_direct.py` applies the three-state update vertex by vertex, exhaustively enumerates every configuration for \(3\le n\le11\), and verifies both period-three eligibility and the phase condition. The independent search covers \(265707\) configurations. Outputs `verify_transfer.out` and `verify_direct.out` record actual successful executions. The finite identity, plus the transfer argument, proves the all-size recurrence; the exhaustive direct dynamics is an independent cross-check, not a substitute for that proof.

## Relationship to prior work

The Greenberg–Hastings excitable update and the concept of stable periodic objects were established in the classical literature. Fisch, Gravner and Griffeath (1991) treated threshold and interaction range, primarily on a two-dimensional lattice. Fisch and Gravner (1995), especially Section 2 and Proposition 2.1, studied stable periodic objects on the one-dimensional lattice with arbitrary interaction range, and explicitly allowed finite intervals with free boundaries. Their stable-object condition covers the present local phase criterion. Gravner, Lyu and Sivakoff (2016), especially Theorem 3, characterized eventual synchronization and activity through cycle integrals on arbitrary graphs. These statements establish general dynamical theory but do not state the cubic finite-length primitive-three census for the open range-two chain.

The new object of the theorem is the compact exact enumeration and third-order recurrence for the full family of finite free-boundary chains, not the existence of periodic objects, the generic phase condition, or a new general cellular-automaton principle.

## Limitations

The result counts only initially primitive period-three states; configurations entering such cycles after a transient are outside scope, as are longer eventual periods. It does not extend the recurrence to range three, periodic spatial boundary conditions, more than three colors, or a higher excitation threshold. The finite identity is independently reproducible from the embedded source; the historical priority check is not proof that no equivalent formula appears in unindexed work. No independent audit has been performed.

## References

1. R. Fisch, J. Gravner and D. Griffeath, “Threshold-range scaling of excitable cellular automata,” *Statistics and Computing* **1** (1991), 23–39. Author-hosted full text: https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf. Open preprint: https://arxiv.org/abs/patt-sol/9304001 (first arXiv submission 1993-04-02).
2. R. Fisch and J. Gravner, “One-dimensional deterministic Greenberg–Hastings models,” *Complex Systems* **9** (1995), 329–348. Full text: https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf.
3. J. Gravner, H. Lyu and D. Sivakoff, “Limiting behavior of 3-color excitable media on arbitrary graphs,” arXiv:1610.07320 (initially submitted 2016-10-24), especially Theorem 3. https://arxiv.org/abs/1610.07320.
