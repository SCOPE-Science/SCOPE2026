# Algebraic recurrent-state growth for majority dynamics on three-row cylinders

## Finding
For every integer \(n\ge 3\), let \(G_n=C_n\square P_3\), with columns indexed by \(\mathbb Z/n\mathbb Z\) and rows indexed by \(\{0,1,2\}\). Let \(F_n\) synchronously update each binary vertex to the strict majority among its *open* neighbours, retaining its current bit in a tie. Define
\[
Q_n=\#\{x:F_n(x)=x\},\qquad P_n=\#\{x:F_n^2(x)=x\}.
\]
Every eventual orbit is a fixed point or a primitive two-cycle. There are explicitly constructed nonnegative integer adjacency matrices \(U\) and \(V\) of respective sizes \(20\) and \(200\), defined below without an unspecified parameter, for which the **exact** all-size census is
\[
Q_n=2+\operatorname{tr}(U^n),\qquad
P_n=2+20\mathbf 1_{2\mid n}+\operatorname{tr}(V^n).
\]
In particular, the number of distinct primitive two-cycles is \((P_n-Q_n)/2\). Both \(U\) and \(V\) are primitive, with respective Perron roots \(\lambda_Q\) and \(\lambda_P\), satisfying the rigorously enclosed intervals
\[
2.2055<\lambda_Q<2.2057,\qquad
3.4578<\lambda_P<3.4580.
\]
Their approximations are \(\lambda_Q\approx2.2055694304\) and \(\lambda_P\approx3.4579127628\). Thus
\[
Q_n\sim\lambda_Q^n,\qquad P_n\sim\lambda_P^n,\qquad
\frac{Q_n}{P_n}\sim\left(\frac{\lambda_Q}{\lambda_P}\right)^n\longrightarrow0.
\]
Therefore almost every *recurrent* configuration belongs to a primitive two-cycle as the cylinder grows. The two Perron roots are algebraic: \(\lambda_Q\) is the real root exceeding two of
\[
\lambda^3-2\lambda^2-1=0,
\]
and \(\lambda_P\) is the unique real root in \((3.4578,3.4580)\) of
\[
\begin{aligned}
&\lambda^{13}-5\lambda^{12}+3\lambda^{11}+10\lambda^{10}-12\lambda^9
+30\lambda^8-41\lambda^7+26\lambda^6\\
&\qquad-97\lambda^5+28\lambda^4+104\lambda^3-28\lambda^2-2\lambda-5=0.
\end{aligned}
\]
The exact sequence begins, for \(n=3,4,5,6,7,8\), with
\[
(Q_n)=(8,36,78,146,260,572),\qquad
(P_n)=(62,402,768,2678,4348,21906).
\]

## Assumptions and scope
The graph is simple. For \(n=3\), the left and right neighbours of a vertex in the cycle are distinct. The two boundary rows have degree three and the middle row has degree four; **only** the middle row can encounter a tied neighbourhood. The three-row width is fixed, but there is no upper bound on circumference \(n\). Counts concern labeled vertex configurations, not rotation classes or initial-condition basin sizes. The claimed period bound applies to *eventual* orbits, not an asserted uniform transient cutoff.

## Proof
### Exact local transfer construction
Encode a column \((x_0,x_1,x_2)\in\{0,1\}^3\) by the integer \(a=\sum_{j=0}^2 2^j x_j\in\{0,\ldots,7\}\). For columns \(a,b,c\), define \(M(a,b,c)\in\{0,\ldots,7\}\) rowwise. In row \(j\), count the two horizontal votes from \(a,c\) and the available vertical votes from \(b\); if the count exceeds half the degree, output one, if less than half, output zero, and if equal, output bit \(b_j\). Thus \(M\) is a completely specified eight-letter radius-one local rule.

Form a directed graph \(A\) on the \(8^2=64\) ordered column-pairs \((a,b)\), with a directed edge
\[
(a,b)\longrightarrow(b,c)\quad\Longleftrightarrow\quad M(a,b,c)=b.
\]
For the second directed graph \(B\), encode a time-pair column as \(w=(a,a')\in\{0,\ldots,7\}^2\), i.e. as \(a+8a'\in\{0,\ldots,63\}\). A vertex is an ordered pair \((w_-,w_0)\), and there is an edge to \((w_0,w_+)\) if and only if both equations
\[
M(a_-,a_0,a_+)=a_0',\qquad
M(a_-',a_0',a_+')=a_0
\]
hold. Thus \(B\) has \(64^2=4096\) specified possible vertices. For each positive integer \(n\), cyclic walks of length \(n\) in \(A\) correspond bijectively to fixed configurations on \(G_n\), so \(Q_n=\operatorname{tr}(A^n)\). Likewise cyclic walks of length \(n\) in \(B\) correspond bijectively to pairs \((x,y)\) with \(F_n(x)=y\), \(F_n(y)=x\); since \(y\) is determined by \(x\), \(P_n=\operatorname{tr}(B^n)\). This is a bijection for every \(n\ge3\), even if a column pattern has smaller spatial period.

An exact finite graph calculation, reconstructed by the accompanying self-contained verifier, identifies the directed strongly connected components that contain cycles. For \(A\), they consist of one 20-vertex strongly connected component and two singleton loops. For \(B\), they consist of one 200-vertex strongly connected component, ten directed two-cycles, and two singleton loops. Define \(U\) and \(V\) as the respective induced adjacency matrices on the unique 20-vertex and 200-vertex components, with vertices sorted by the integer encodings above. A closed walk is contained entirely in one strongly connected component. The component counts therefore imply the exact displayed formulas for \(Q_n\) and \(P_n\). They also specify \(U,V\) constructively and without any external matrix table.

### Exact finite algebra and asymptotics
The attached verifier regenerates \(A,B,U,V\), determines their strongly connected components using a separate finite graph algorithm, and computes \(\det(I-zU)\) and \(\det(I-zV)\) by the exact Newton identities
\[
c_0=1,\qquad k c_k=-\sum_{j=1}^k c_{k-j}\operatorname{tr}(T^j)
\quad(1\le k\le\dim T).
\]
It verifies the complete factorizations, not just values for sampled circumferences. The determinant for \(U\) has degree \(16\), and that for \(V\) has degree \(72\); in both cases the remaining coefficients vanish exactly. Among the irreducible factors of the two determinants are respectively \(1-2z-z^3\) and
\[
-1+5z-3z^2-10z^3+12z^4-30z^5+41z^6-26z^7+97z^8-28z^9-104z^{10}+28z^{11}+2z^{12}+5z^{13}.
\]
Substitution \(z=\lambda^{-1}\) produces the stated characteristic equations. Exact integer graph checks establish that \(U\) and \(V\) are strongly connected and aperiodic, hence primitive. To enclose their Perron roots, apply each adjacency matrix 60 times to the all-ones vector \(v\), then compute \(Tv\): the verifier checks the strict rational coordinate inequalities \(2.2055v<Tv<2.2057v\) for \(U\), and \(3.4578v<Tv<3.4580v\) for \(V\). Collatz--Wielandt proves the spectral enclosures, and the checked determinant factors identify the corresponding positive roots. Perron--Frobenius then gives \(\operatorname{tr}(U^n)\sim\lambda_Q^n\) and \(\operatorname{tr}(V^n)\sim\lambda_P^n\), with leading coefficient one. The remaining bounded component contributions do not affect these asymptotics.

### Why eventual periods are at most two
For a binary configuration in signs \(s(t)\in\{-1,1\}^{V(G_n)}\), set \(H=A_{G_n}+\tfrac12 I\), with \(A_{G_n}\) the symmetric adjacency matrix. Since all open-neighbour sums are integers, the majority-with-tie-retention update is precisely \(s_i(t+1)=\operatorname{sign}((Hs(t))_i)\), and no entry of \(Hs(t)\) is zero. Define \(E(t)=-s(t)^\top Hs(t-1)\). Symmetry gives
\[
E(t+1)-E(t)=\sum_i [s_i(t-1)-s_i(t+1)](Hs(t))_i\le0,
\]
with strict inequality whenever \(s(t+1)\ne s(t-1)\). On a finite state space the possible values of \(E\) are finite, so eventually \(s(t+1)=s(t-1)\). Hence every eventual orbit has period dividing two. This argument does not assume odd vertex degrees.

## Verification
The standalone Python program `verify.py` uses only standard-library integer arithmetic. It constructs all admissible triples, checks the recurrent strongly connected components and their graph periods, calculates and verifies exact characteristic determinant factorizations via Newton identities, and proves the spectral radius brackets using positive integer vectors. A separately coded site-by-site update independently counts all \(2^{3n}\) configurations for every \(n=3,4,5,6\); results coincide with the transfer-matrix counts. The emitted output is included as `verification_output.txt`. Reproduce with `python3 verify.py`.

## Relationship to prior work
The general theorem that synchronous symmetric threshold dynamics eventually has period at most two is classical (Goles and Olivos, 1980); no general period bound is claimed as new. Jen (1988) introduced a broadly applicable cylindrical cellular-automaton transfer-matrix approach; the use of a transfer matrix alone is not presented as novel. The 2013 work of Lemoy, Mozeika and Seki treats a noisy one-dimensional self-inclusive majority automaton, not open-neighbour majority with mixed odd/even degrees on a cylindrical three-row graph. The present contribution is the explicit **mixed-degree three-row** exact census, the finite determinant factors, and two distinct algebraic growth constants proving overwhelming two-cycle recurrence. A prior exact census for two-row circular prisms has a different graph, uniformly odd vertex degrees, and therefore no tie-retention mechanism in its interior; those formulas do not imply these coefficients or growth constants.

## Limitations
No formula for attraction-basin sizes, transient depths, or cylinders of other widths is asserted. The exact finite determinant verification is computer-assisted but reconstructible from the included standalone code; brute force for small \(n\) is corroboration only, not proof for all \(n\). The full text of Jen's 1988 article was not accessible during this comparison; its available abstract describes the general transfer method and closed expressions for two-neighbour rules. This access limitation and the possibility of an unindexed special-case enumeration remain originality risks. Independent scientific audit has not been performed.

## References
- E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187--189, DOI: 10.1016/0012-365X(80)90121-1.
- E. Jen, *Cylindrical cellular automata*, Communications in Mathematical Physics 118 (1988), 569--590, DOI: 10.1007/BF01221109.
- R. Lemoy, A. Mozeika, and S. Seki, *Transfer matrix analysis of one-dimensional majority cellular automata with thermal noise*, arXiv:1311.4388v1 (publicly posted 2013-11-18); Journal of Physics A 47 (2014), 105001.
- Z. Agur, A. S. Fraenkel, and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295--302, DOI: 10.1016/0012-365X(88)90005-2.
