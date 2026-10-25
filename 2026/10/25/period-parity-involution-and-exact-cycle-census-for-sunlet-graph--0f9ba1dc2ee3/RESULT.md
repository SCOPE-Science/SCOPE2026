# Period-parity involution and exact cycle census for sunlet-graph XOR dynamics

## Finding

Let \(H_n\), for each integer \(n\ge 3\), be the sunlet graph obtained by attaching one leaf to each vertex of the cycle \(C_n\). Simultaneously replace every binary vertex state by the exclusive-or (sum over \(\mathbb F_2\)) of the states of all its graph neighbours. Write \(F_n\) for this operator on the \(2n\)-dimensional binary state space.

**Theorem (full period census and an affine period-doubling symmetry).** For every \(n\ge3\) and positive integer \(t\), put \(g=\gcd(n,t)\). The number of configurations fixed after exactly \(t\) updates is
\[
|\operatorname{Fix}(F_n^t)|=\begin{cases}
2^{2g-1},&n\text{ and }t\text{ both odd},\\
2^{2g},&\text{otherwise}.
\end{cases}
\]
The transformation is invertible; its exact order is \(n\) for even \(n\) and \(2n\) for odd \(n\). Thus every state is periodic from time zero.

Let \(\mu\) denote the Möbius function and set
\[
M(d)=\sum_{e\mid d}\mu(d/e)4^e\qquad(d\ge1).
\]
For even \(n\), a positive integer \(t\) can be a primitive period only if \(t\mid n\); in that case the number of **states** of primitive period \(t\) is exactly \(M(t)\), and the number of primitive cycles is \(M(t)/t\). For odd \(n\), the only possible primitive periods are \(d\) and \(2d\), where \(d\mid n\). For each such \(d\), the number of states of period \(d\) and the number of states of period \(2d\) are *equal* and both are exactly \(M(d)/2\); the respective numbers of cycles are \(M(d)/(2d)\) and \(M(d)/(4d)\).

More strongly, for every odd \(n\), write states as \(z=(x,y)\in\mathbb F_2^n\times\mathbb F_2^n\), with \(x\) on cycle vertices and \(y\) on their attached leaves, and define
\[
\pi(z)=\sum_{i=0}^{n-1}(x_i+y_i)\pmod2,\qquad
E=(\mathbf1,\mathbf0).
\]
Then \(\pi(z)=0\) if and only if the primitive period of \(z\) is odd. The explicit affine involution \(z\mapsto z+E\) exchanges, for **every** divisor \(d\mid n\), *all* primitive-period-\(d\) states bijectively with all primitive-period-\(2d\) states. This is an actual statewise period-doubling correspondence, not merely equality of two counts.

## Assumptions and scope

Every graph is finite, undirected and simple; \(n\ge3\), so the two cycle neighbours of each cycle vertex are distinct. All sums and matrix operations are over \(\mathbb F_2\). There is no asynchronous scheduling, nonbinary alphabet, external input, boundary truncation or weighted edge. If \(S\) denotes the cyclic shift on \(\mathbb F_2^n\), then the whole map is
\[
F_n(x,y)=((S+S^{-1})x+y,x),\qquad
F_n^{-1}(u,v)=(v,u+(S+S^{-1})v).
\]
The term \(M(d)\) is the standard primitive-word Möbius count for a four-letter alphabet; its use here is an exact numerical correspondence, not an assertion that these two permutation systems are canonically conjugate. Nothing is claimed about every graph containing a cycle, nor about transient dynamics: all states of this particular reversible map are recurrent.

## Proof

**1. Laurent-polynomial representation.** Put \(R=\mathbb F_2[s,s^{-1}]/(s^n+1)\) and \(B=s+s^{-1}\). Relative to the two cyclic vertex classes, \(F_n\) is multiplication by
\[
T=\begin{pmatrix}B&1\\1&0\end{pmatrix}
\]
on \(R^2\). Define Laurent polynomials \(P_0=0\), \(P_1=1\), and \(P_{t+1}=BP_t+P_{t-1}\) for \(t\ge1\). Induction gives
\[
P_t(B)=\sum_{j=0}^{t-1}s^{t-1-2j}
=s^{-(t-1)}\left(\frac{s^t+1}{s+1}\right)^2,
\quad T^t=\begin{pmatrix}P_{t+1}&P_t\\P_t&P_{t-1}\end{pmatrix}.
\]
Here the displayed fraction is an **ordinary polynomial quotient**, since \(s+1\) divides \(s^t+1\) in characteristic two. Multiplying \(T\) by the matrix with diagonal entries zero and off-diagonal entries one verifies \(\det T=1\). Since the characteristic polynomial of \(T\) factors as \((\lambda+s)(\lambda+s^{-1})\) over the Laurent ring, the power-sum trace recurrence gives \(\operatorname{tr}(T^t)=s^t+s^{-t}\) (no diagonalizability is assumed). Therefore
\[
\det(T^t-I)=s^t+s^{-t}=s^{-t}(s^t+1)^2.
\]

**2. The two Smith invariant factors.** Work initially over the Laurent polynomial PID \(\mathbb F_2[s,s^{-1}]\), *before* reducing modulo \(s^n+1\). The entries \(P_{t+1}+1\) and \(P_{t-1}+1\), modulo the off-diagonal entry \(P_t\), both reduce to the associate \(s^t+1\): indeed \(P_{t+1}=sP_t+s^{-t}\) and \(P_{t-1}=s^{-1}P_t+s^{-t}\). Thus the first Smith divisor is
\[
D_1\sim\gcd(P_t,s^t+1).
\]
Let \(H_t=(s^t+1)/(s+1)\). Since \(P_t\sim H_t^2\), a root-multiplicity calculation yields
\[
D_1\sim \begin{cases}s^t+1,&t\text{ even},\\H_t,&t\text{ odd}.
\end{cases}
\]
For precision, when \(t=2^r u\) with \(u\) odd, \(s^t+1=(s^u+1)^{2^r}\), and \(H_t\) has \((s+1)\)-multiplicity \(2^r-1\) and every other root's full multiplicity \(2^r\). For even \(t\), squaring supplies at least the \(2^r\) central multiplicity needed for the gcd; for odd \(t\), the central root is absent from \(H_t\) altogether. Other irreducible factors contribute their full degree in either case.

Dividing the determinant by this first divisor gives the second Smith divisor, hence
\[
(D_1,D_2)\sim\begin{cases}
(s^t+1,\ s^t+1),&t\text{ even},\\
((s^t+1)/(s+1),\ (s^t+1)(s+1)),&t\text{ odd}.
\end{cases}
\]
Unimodular row/column operations over the Laurent PID remain invertible after quotienting by \(s^n+1\). Multiplication by a polynomial \(D\) on \(R\) has binary kernel dimension \(\deg\gcd(D,s^n+1)\). Consequently, the fixed-space dimension is the sum of these two gcd degrees.

**3. Fixed spaces and exact order.** The familiar identity \(\gcd(s^t+1,s^n+1)=s^{\gcd(n,t)}+1\) holds in \(\mathbb F_2[s]\). When \(t\) is even, the two Smith divisors give dimension \(2g\). When \(t\) is odd, at all roots other than \(s=1\) the two gcd contributions still total twice their common multiplicity. At \(s=1\), the first divisor has no factor and the second has exactly two; this contributes two when \(n\) is even (the modulus has multiplicity at least two) but just one when \(n\) is odd (the modulus is squarefree at this root). Thus the dimension is \(2g\) except for the single-unit deficit when \(n,t\) are both odd. Taking powers of two proves the fixed-state formula.

Since the ambient space has dimension \(2n\), \(F_n^t\) is the identity exactly when this fixed dimension reaches \(2n\). The least such positive \(t\) is \(n\) for even \(n\) and \(2n\) for odd \(n\). Invertibility was already established by the explicit inverse.

**4. Primitive orbit populations.** For any permutation of a finite set, the number of states with primitive period exactly \(t\) is \(\sum_{e\mid t}\mu(t/e)|\operatorname{Fix}(F_n^e)|\). If \(n\) is even and \(d\mid n\), then every \(e\mid d\) has \(\gcd(n,e)=e\), yielding \(M(d)\). If \(n\) is odd and \(d\mid n\), every \(e\mid d\) is odd, so the odd-period population is \(M(d)/2\). The full \(2d\)-fixed set has cardinality \(4^d\), while its \(d\)-fixed subset has cardinality \(4^d/2\). Möbius inversion applied to their difference yields the equal \(2d\)-period population \(M(d)/2\). Other periods are impossible because their lengths divide the order of \(F_n\). Each orbit of length \(t\) comprises \(t\) distinct states, so division by \(t\) completes the cycle census.

**5. A parity-selected affine involution for odd \(n\).** Define \(J=1+s+\cdots+s^{n-1}\in R\). When \(n\) is odd, multiplication by two permutes residue classes modulo \(n\), hence the explicit sum in Step 1 gives \(P_n=J\). Also \(sJ=J\) and \(s^n=1\) in \(R\), so \(P_{n+1}=P_{n-1}=J+1\). Consequently
\[
T^n=I+\begin{pmatrix}J&J\\J&J\end{pmatrix}.
\]
Multiplication by \(J\) sends a binary word to its coordinate sum times the all-one word. Thus
\[
F_n^n(z)=z+\pi(z)W,\qquad W=(\mathbf1,\mathbf1).
\]
The parity \(\pi\) is invariant because the XOR-neighbour contribution from each cycle vertex is counted twice. For \(\pi(z)=0\), the period divides odd \(n\); for \(\pi(z)=1\), \(F_n^n(z)\ne z\), so the period is even (and divides \(2n\)). Moreover \(F_n(E)=E+W\), with \(F_n(W)=W\). For all \(t\ge0\), \(F_n^t(E)=E+(t\bmod2)W\). Since \(n\) is odd, \(\pi(E)=1\), and translation by \(E\) interchanges the two parity classes. If \(z\) has odd period \(d\), then \(z+E\) has period precisely \(2d\): no odd return is possible, while time \(2d\) returns it. Conversely, if \(z\) has period \(2d\), then \(z+E\) has odd period dividing \(d\); if it were a proper divisor, translating again would contradict the primitive period \(2d\). Translation by \(E\) is its own inverse, proving a bijection at every \(d\mid n\).

## Verification

Run \(`python3 verify.py`\) using the standard Python 3 library from the directory containing that script. The script independently constructs the graph update over labelled vertices and checks the rank of \(F_n^t-I\) in **2,346** cases (\(3\le n\le48\), \(1\le t\le2n\)) and the exact orders at **46** graph sizes. It separately compares the two stated Smith polynomial gcd degrees in **3,040** cases. Exhaustive orbit enumeration for \(3\le n\le9\) covers **349,504** labelled configurations and compares the computed primitive cycles with Möbius predictions in **29** period cases. For odd graph sizes it additionally checks period parity and the explicit bitwise-complement bijection on every labelled state, with sampled iteration checks of the identity for \(F_n^n\). The program prints \(`SUNLET_PARITY_VERIFY_OK`\) on success. The accompanying \(`verification_output.txt`\) records its output.

These finite computations corroborate, but **do not replace**, the arbitrary-size algebraic proof above. The \(n=3\) period-cycle counts are \(2\) fixed points, \(1\) two-cycle, \(10\) three-cycles and \(5\) six-cycles; these account for all \(64\) states. For \(n=4\), the counts are \(4\), \(6\) and \(60\) cycles of periods \(1,2,4\), respectively, accounting for all \(256\) states.

## Relationship to prior work

Martin, Odlyzko and Wolfram (1984) developed the Laurent-polynomial approach for additive cellular automata, including higher-order reversible dynamics. Their discussion of second-order rule-90 already supplies period bounds; the period order alone is **not** offered as new here. Kawahara and Lee's dated 1995 report defines a map of the same memory form and proves period bounds and symmetry criteria on finite **null-boundary** one-dimensional arrays (Theorem 4.2). Its one-dimensional configuration space has \(m-1\) interior sites, rather than the \(n\)-site circular geometry considered here. Its main theorems do not state the sunlet orbit-by-orbit arithmetic census or the affine period-doubling involution. Vlasov (2014) gives the same reversible memory construction in an infinite-lattice setting and studies spatial propagation, not this finite orbit census.

Guan and He (1986) is **particularly relevant** because its abstract expressly describes general cycle-length and multiplicity formulas for higher-order finite additive cellular automata. The full paper could not be inspected; the present explicit arithmetic specialization and constructive affine pairing must be distinguished from that general framework. The mathematical mechanism needed here includes a local Smith-factor computation at the central binary frequency and a statewise parity involution. The existence of an equivalent earlier specialization, or of a previously published general theorem that transparently gives every claimed item, remains a material literature-overlap risk.

## Limitations

This theorem is confined to the sunlet graph with uniform binary XOR-neighbour updates. The arithmetic count equality for even \(n\) with four-letter cyclic word rotations is an equality of cycle counts, not a demonstrated canonical linear conjugacy. No extension to nonlinear updates, stochastic excitation, general trees with leaves, or infinite-volume dynamics is claimed. Independent external verification has not been performed. Inaccessible historically relevant full text (especially Guan–He 1986) limits the strength of the novelty comparison; no historical uniqueness is claimed.

## References

1. O. Martin, A. M. Odlyzko and S. Wolfram, “Algebraic Properties of Cellular Automata,” *Communications in Mathematical Physics* **93** (1984), 219–258. DOI: 10.1007/BF01223745.
2. P.-h. Guan and Y. He, “Exact Results for Deterministic Cellular Automata with Additive Rules,” *Journal of Statistical Physics* **43** (1986), 463–478. DOI: 10.1007/BF01020648.
3. Y. Kawahara and H. Y. Lee, “Period Lengths of Cellular Automata cam-90 with Memory,” RIFIS Technical Report **119** (dated 1995-10-25), Kyushu University Institutional Repository, https://hdl.handle.net/2324/3220; later *Journal of Mathematical Physics* **38** (1997), 255–266, DOI: 10.1063/1.531841.
4. A. Yu. Vlasov, “Reversible Cellular Automata and Quantum Computers,” arXiv:1407.6553 (initial submission 2014-07-24), https://arxiv.org/abs/1407.6553.
