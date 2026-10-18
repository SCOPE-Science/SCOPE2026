# Sharp positive Fourier quadrature for four consecutive sites on cyclic prime-power groups

## Finding
Let \(N=p^k\ge4\) be a prime power, let \(G=\mathbb Z/N\mathbb Z\), and consider the four spatial sites \(A=\{0,1,2,3\}\). A *positive Fourier quadrature* is a set \(B\subseteq G\) of distinct frequency residues with weights \(w_b>0\) such that the vectors
\[
\bigl(\sqrt{w_b}\,e^{2\pi i ba/N}\bigr)_{a\in A},\qquad b\in B,
\]
form a Parseval frame for \(\mathbb C^A\) with its counting inner product. If \(\nu(N)\) is the least cardinality of such a set, then
\[
\boxed{\nu(p^k)=\begin{cases}
4,&p=2,\ k\ge2,\\
5,&p=5,\ k\ge1,\\
7,&p=3,\ k\ge2,\ \text{or }p\ge7,\ k\ge1.
\end{cases}}
\]
The minimizing configurations are completely rigid in both exceptional prime families: at powers of two, every four-node rule is a translate of the order-four frequency subgroup with all weights \(1/4\); at powers of five, every five-node rule is a translate of the order-five frequency subgroup with all weights \(1/5\). At the other stated prime powers, a seven-node positive rule always exists.

A decisive obstruction is the **middle elementary-symmetric condition**: every such rule on \(m\in\{4,5,6\}\) distinct frequencies satisfies
\[
\sum_{\substack{I\subseteq B\\|I|=3}}
\exp\!\left(\frac{2\pi i}{N}\sum_{b\in I}b\right)=0.
\]
For prime powers this forces \(p\mid\binom m3\). Thus the first three potential quadrature sizes \(4,5,6\) are arithmetically forbidden simultaneously whenever \(p=3\) or \(p\ge7\); the remaining exceptional size \(5\) at powers of five has the above exact coset rigidity.

## Assumptions and scope
Frequencies are **distinct** residues of \(G\), not a multiset. All weights must be strictly positive real numbers. The four spatial sites are distinct because \(N\ge4\). We normalize the frame bound to one; any positive common rescaling yields a tight frame. Put \(z_b=e^{2\pi i b/N}\). The row Gram matrix of the proposed analysis operator is the identity precisely when
\[
\sum_{b\in B}w_b=1,\qquad
\sum_{b\in B}w_bz_b^t=0\quad(t=1,2,3).
\tag{1}
\]
The negative-moment equations follow from reality of the weights. Translating the spatial sites or multiplying them by an invertible residue yields the corresponding equivalent statement after relabeling frequencies. The theorem does not address non-prime-power moduli or nonconsecutive four-site patterns.

## Proof
**1. Fourier moments and the degree-six polynomial certificate.** Equation (1) follows by computing the four-by-four row Gram matrix: its \((a,a')\) entry is \(\sum_b w_b z_b^{a-a'}\). In particular \(m=|B|\ge4\), by rank.

Suppose \(4\le m\le6\) and list the distinct nodes as \(z_1,\ldots,z_m\). Form the monic polynomial
\[
P(Z)=\prod_{j=1}^m(Z-z_j)
=Z^m-e_1Z^{m-1}+e_2Z^{m-2}-e_3Z^{m-3}+\cdots,
\]
and \(Q(Z)=Z^{6-m}P(Z)\), a degree-six polynomial vanishing at every node. Write \(Q(Z)=\sum_{t=0}^6c_tZ^t\). For each \(t\in\{0,1,2,4,5,6\}\), the number \(t-3\) is a nonzero integer of modulus at most three, so (1) gives
\[
0=\sum_{j=1}^mw_jz_j^{-3}Q(z_j)
=\sum_{t=0}^6c_t\sum_{j=1}^mw_jz_j^{t-3}=c_3=-e_3.
\tag{2}
\]
Hence the third elementary symmetric polynomial \(e_3=\sum_{i<j<\ell}z_iz_jz_\ell\) is zero.

**2. Cyclotomic length obstruction.** Each of the \(\binom m3\) summands of \(e_3\) is an \(N\)-th root of unity, with repetitions allowed. Since \(N=p^k\), any vanishing sum of \(N\)-th roots with nonnegative integer multiplicities has a number of summands divisible by \(p\). This may be seen directly: reduce exponents modulo \(N\), write the corresponding polynomial \(F\in\mathbb Z[X]\) with \(\deg F<N\), and use \(\Phi_N\mid F\); evaluating at one gives \(p=\Phi_N(1)\mid F(1)\). It is also the prime-power case of the vanishing-sum theorem of Lam and Leung [1]. Thus
\[
p\mid\binom m3\in\{4,10,20\},\qquad m=4,5,6.
\tag{3}
\]
For \(p=3\) or \(p\ge7\), (3) excludes every size below seven. For \(p=5\), it excludes four; for \(p=2\), the rank bound already excludes fewer than four.

**3. Positive constructions and sharpness.** At \(p=2\), take the order-four subgroup of frequencies \(B=\{0,N/4,N/2,3N/4\}\) with weights \(1/4\). Its first three moments vanish, so \(\nu(N)=4\). At \(p=5\), take the order-five subgroup \(B=\{0,N/5,2N/5,3N/5,4N/5\}\) with weights \(1/5\), giving \(\nu(N)=5\).

For \(p=3\) and \(k\ge2\), or for \(p\ge7\), we have \(N\ge7\). Map each \(N\)-th root \(z\) to
\[
\Phi(z)=\bigl(\Re z,\Im z,\Re z^2,\Im z^2,\Re z^3,\Im z^3\bigr)\in\mathbb R^6.
\]
The uniform average of \(\Phi(z)\) over all \(N\)-th roots is zero, since \(N>3\). Carathéodory's theorem in dimension six places zero in the convex hull of at most seven such vectors. Discard zero weights, leaving strictly positive real weights on distinct nodes. Equation (1) then holds. The lower bound from Step 2 excludes any rule with fewer than seven nodes; the resulting rule therefore has exactly seven. This establishes the cardinality formula for every prime power in the stated domain.

**4. Rigidity of four-node minimizers at powers of two.** With exactly four columns, a Parseval analysis matrix is a square unitary matrix. Each of its four columns has squared Euclidean norm \(4w_j\), forcing \(w_j=1/4\). Pairwise column orthogonality says that the ratio \(r=z_i/z_j\ne1\) obeys \(1+r+r^2+r^3=0\). Its possible values are the three nontrivial fourth roots of unity. Fixing one node, the other three must therefore be its three distinct fourth-root multiples. All nodes constitute exactly a coset of the order-four subgroup; this also shows all such cosets attain the bound.

**5. Rigidity of five-node minimizers at powers of five.** Let \(N=5^k\), put \(H=5^{k-1}\), and suppose \(B=\{b_1,\ldots,b_5\}\) supports a five-node positive rule. Step 1 gives \(e_3(z_1,\ldots,z_5)=0\). Since every node is nonzero,
\[
0=\frac{e_3(z_1,\ldots,z_5)}{\prod_jz_j}
=\sum_{1\le i<j\le5}(z_iz_j)^{-1}.
\tag{4}
\]
For every residue \(r\pmod H\), count the ten unordered pairs \(\{i,j\}\) with \(-b_i-b_j\equiv r\pmod H\). The cyclotomic polynomial \(\Phi_{5^k}(X)=1+X^H+X^{2H}+X^{3H}+X^{4H}\) divides the integer mask polynomial of (4). Because that mask has degree less than \(5H\), its five coefficients in each residue class \(r\pmod H\) are equal; therefore **each** residue-class count of pair sums modulo \(H\) is divisible by five. Their total is ten, so at most two different pair-sum residue classes occur.

Set \(a_j=b_j\pmod H\). If three distinct values \(a,b,c\) occurred among these five residues, the three pair sums \(a+b,a+c,b+c\) would be distinct, contradicting the two-class bound. Suppose exactly two values \(a\ne b\) occur. If each appears at least twice, the three sums \(2a,a+b,2b\) all occur and are pairwise distinct because \(H\) is odd; this is again impossible. Otherwise the multiplicities are one and four, and the only pair-sum classes occur with multiplicities four and six, neither divisible by five. Therefore all five residues \(b_j\pmod H\) are equal.

Exactly five distinct frequencies belong to that residue class, hence \(B\) is the complete coset \(\{r,r+H,r+2H,r+3H,r+4H\}\pmod N\) of the order-five subgroup. After translating frequencies, equations (1) annihilate every nontrivial fifth-order Fourier character: degrees \(1,2,3\) and their negatives exhaust the four such characters. Fourier inversion on the five-point group forces all five weights to equal \(1/5\). Conversely every such coset with these weights is a positive Parseval rule. This completes the rigidity classification.

## Verification
The standalone standard-library checker `verify.py` implements exact prime-power cyclotomic zero tests by integer coefficient counts. It exhaustively checks every five-frequency subset of \(\mathbb Z/25\mathbb Z\), finding that exactly the five order-five cosets satisfy the necessary polynomial condition (2); it checks every four-, five-, and six-frequency subset of \(\mathbb Z/9\mathbb Z\) and \(\mathbb Z/7\mathbb Z\), finding none with (2); and it checks exact vanishing moments on the subgroup constructions. The completed replay reports `EXACT_CHECKS_PASS tested_patterns=53538 order25_optimizers=5`.

For additional, non-certificate corroboration, solving the seven real moment equations by linear programming yields strictly positive seven-node rules on \(\mathbb Z/9\mathbb Z\), \(\mathbb Z/11\mathbb Z\), \(\mathbb Z/27\mathbb Z\), and \(\mathbb Z/49\mathbb Z\). Numerical LP is not needed for the proof: Carathéodory gives existence in all cases, while Steps 1–2 supply the infinite lower bound. The rigidity argument is exact and does not rely on a finite search.

## Relationship to prior work
Lam and Leung [1] give the root-of-unity vanishing-sum obstruction, here applied to the middle elementary-symmetric polynomial of a quadrature support; their theorem does not classify the weighted four-site designs. Weighted Fourier Parseval frames appear in the self-affine setting of Dutkay and Ranasinghe [2]. Frederick and Mayeli [3] develop frame spectral pairs and transfer constructions for finite Fourier sets, but their inspected main results do not identify this four-site prime-power cardinality-and-rigidity law. A published three-site positive Fourier sampling theorem [4] has a different arithmetical phase diagram and does not cover four sites: increasing the moment order changes the symmetric obstruction from six-term to four-, ten-, and twenty-term root sums, and produces the rigid prime-five branch proved above. A separate published prime-power theorem [5] determines the minimum cardinality when **all** frequency weights are equal. The variable-positive-weight problem here is different: for instance, the seven-node bound stays fixed at primes above five although the equal-weight minimum grows with the prime.

## Limitations
This is a theorem for **exact** Parseval tightness with arbitrary positive weights, not a stability theorem for approximately tight frames. The seven-node case is an existence classification, not a list of all optimal seven-node supports or their weights; Carathéodory is nonconstructive. The two exceptional low-cardinality branches are fully classified. The theorem only treats cyclic prime-power groups and a four-term unit-step arithmetic progression. The publicly inspected related sources do not settle the same weighted law, but an older equivalent result under finite trigonometric quadrature terminology remains a literature risk. The finite checker is corroborative; no computer enumeration is used to infer an infinite impossibility.

## References
1. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209v1 (first publicly posted 1995-11-13), later Journal of Algebra 224 (2000), 91–109.
2. D. E. Dutkay and R. Ranasinghe, *Weighted Fourier Frames on Self-Affine Measures*, arXiv:1710.01224v1 (first posted 2017-10-03).
3. C. Frederick and A. Mayeli, *Frame spectral pairs and exponential bases*, arXiv:2010.05667v1 (first posted 2020-10-12).
4. *Sharp positive Fourier sampling on three consecutive cyclic sites*, publicly accessible at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-positive-fourier-sampling-on-three-consecutive-cyclic-site--29fa16b8c55a.
5. *Minimum tight exponential-frame size on cyclic prime-power groups*, publicly accessible at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-minimum-tight-exponential-frame-size-on-cyclic-prime-power-group--b7a941dc4a7d.
