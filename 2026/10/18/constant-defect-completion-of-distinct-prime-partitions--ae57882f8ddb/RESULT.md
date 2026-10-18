# Constant-defect completion of distinct-prime partitions

## Finding
Let \(p_j\) be the \(j\)-th prime and \(S_j=\sum_{i=1}^j p_i\), with \(S_0=0\). Put \(k(n)=\max\{j:S_j\le n\}\). For a finite prime set \(A\), put \(s(A)=\sum_{p\in A}p\), \(v(A)=\prod_{p\in A}p\), with the empty product equal to one. Let \(L(n)\) be the greatest \(|A|\) with \(s(A)=n\), and let \(M(n)=\max_{s(A)=n}v(A)\), \(H(n)=\max_{s(A)\le n}v(A)\). The quantities \(L(n)\) and \(M(n)\) are defined for all sufficiently large \(n\) by the theorem below. Let \(K(n)\) be the number of prime factors of the unique squarefree product \(M(n)\).

**Theorem.** For every sufficiently large positive integer \(n\),
\[
0\le k(n)-L(n)\le2,\qquad
1\le\frac{H(n)}{M(n)}\le p_{k(n)+1}^{6}\le(2n)^6.
\]
Furthermore, in the parity class \(n\equiv k(n)\pmod2\), the deficit is completely determined:
\[
L(n)=\begin{cases}
k(n),&n=S_{k(n)+1}-2,\\
k(n)-1,&n\ne S_{k(n)+1}-2.
\end{cases}
\]
Finally \(K(n)\sim L(n)\sim k(n)\sim2\sqrt{n/\log n}\) and \(\log M(n)\sim\sqrt{n\log n}\). The constant two bounds the number of missing parts, while the exponent six bounds the multiplicative cost of replacing an inequality constraint by exact equality. Neither constant is asserted to be globally optimal.

## Assumptions and scope
Every prime set has pairwise distinct ordinary positive primes, including the prime two when present. The result holds for **every** sufficiently large integer of either parity. It relies on established unconditional theorems: the 2017 near-equal three-primes theorem including the residue-class-uniform construction in its proof, the 2015 bounded-sum primorial envelope, Bertrand's postulate, and the prime number theorem. No Goldbach conjecture or assumed prime-gap estimate is used.

## Proof
**1. A distinct near-equal ternary-prime lemma.** We first extract a distinctness refinement of the argument of Matomäki–Maynard–Shao [3, proof of Theorem 2.1 and §3]. For any fixed \(\theta\in(11/20,1)\), all sufficiently large odd integers \(R\) admit a decomposition \(R=q_1+q_2+q_3\) into **pairwise distinct primes** satisfying \(|q_i-R/3|=O(R^\theta)\). A constant multiple in the interval from [3] is absorbed by first choosing an exponent strictly between \(11/20\) and \(\theta\).

Here is the distinctness justification, which is essential because the headline statement of [3, Theorem 1.1] by itself does not require distinct primes. In [3, proof of Theorem 2.1], set \(W=\prod_{p\le w}p\), with \(w=0.1\log\log R\); the argument works uniformly for **any** reduced residue classes \(b_1,b_2,b_3\pmod W\) satisfying \(b_1+b_2+b_3\equiv R\pmod W\). For all sufficiently large \(R\), \(7\mid W\). For each residue of \(R\pmod7\), the following three distinct nonzero residues modulo seven have that sum:
\[
\begin{array}{c|ccccccc}
R\bmod7&0&1&2&3&4&5&6\\\hline
(b_1,b_2,b_3)\bmod7&(1,2,4)&(1,2,5)&(1,2,6)&(1,3,6)&(1,4,6)&(1,5,6)&(1,2,3).
\end{array}
\]
For each other odd prime \(\ell\mid W\), choose three nonzero residues having prescribed sum \(R\pmod\ell\): this is possible for every \(\ell\ge3\), since the sumset of three copies of \((\mathbb Z/\ell\mathbb Z)^\times\) is the whole residue ring. Modulo two choose \((1,1,1)\), which sums to odd \(R\). The Chinese remainder theorem then supplies the required three reduced classes modulo \(W\), pairwise distinct modulo seven. The published argument [3, proof of Theorem 2.1] constructs primes in exactly those chosen classes, proving they are pairwise distinct and lie in the near-equal interval. The finite residue check and use of arbitrary admissible classes are the only modifications of [3].

**2. Uniform two-part deficit.** Let \(k=k(n)\). By the prime number theorem \(k\sim2\sqrt{n/\log n}\). Choose \(t\in\{4,5\}\) so that \(j=k-t\equiv n\pmod2\), possible for every \(n\), and assume \(n\) sufficiently large that \(j\ge2\). Since \(S_j\equiv j-1\pmod2\), the remainder \(R=n-S_j\) is odd. As \(S_k\le n<S_{k+1}\),
\[
tp_j\le\sum_{i=j+1}^{k}p_i\le R<\sum_{i=j+1}^{k+1}p_i\le(t+1)p_{k+1}.
\]
For fixed \(t\), the prime number theorem gives \(p_{k+1}/p_j\to1\), so \(R\asymp p_j\to\infty\). With any fixed \(\theta\in(11/20,1)\), the three distinct primes from Step 1 satisfy
\[
q_i\ge R/3-O(R^\theta)\ge (t/3-o(1))p_j>p_j
\]
since \(t\ge4\). Consequently \(\{p_1,\ldots,p_j,q_1,q_2,q_3\}\) is a distinct-prime partition with **exact sum** \(n\) and \(j+3=k-t+3\) parts. Any \(\ell\) distinct primes have sum at least \(S_\ell\), so \(L(n)\le k\). Hence \(0\le k-L(n)\le t-3\le2\).

**3. Exact parity classification.** If \(n\equiv k\pmod2\), we choose \(t=4\), so the preceding construction gives \(L(n)\ge k-1\). A sum of \(k\) distinct primes **containing two** has parity \(k-1\), which cannot equal \(n\). Therefore any length-\(k\) representation must use \(k\) odd primes, whose sum is at least \(3+5+\cdots+p_{k+1}=S_{k+1}-2\). But \(n<S_{k+1}\) by the definition of \(k\), and \(n\equiv k\equiv S_{k+1}\pmod2\). Therefore length \(k\) is possible exactly when \(n=S_{k+1}-2\); in that case \(\{p_2,\ldots,p_{k+1}\}\) attains it. Otherwise \(L(n)=k-1\).

**4. Constant-cost product completion.** Let \(P_j=\prod_{i=1}^jp_i\). The proven bounded-sum primorial envelope of Deléglise–Nicolas [2, Proposition 1] states \(P_k\le H(n)\le P_{k+1}\). Step 2 produces an exact-sum partition with product at least \(P_j\). Hence
\[
1\le H(n)/M(n)\le P_{k+1}/P_j=\prod_{i=j+1}^{k+1}p_i\le p_{k+1}^{t+1}\le p_{k+1}^6\le(2n)^6.
\]
The last bound follows from Bertrand's postulate and \(p_k\le n\). The prime number theorem implies \(\log P_k\sim\sqrt{n\log n}\), and the displayed sandwich shows \(\log M(n)\sim\sqrt{n\log n}\).

**5. Part count of the product maximizer.** By AM–GM, \(M(n)\le(n/K(n))^{K(n)}\). If there were a fixed \(\varepsilon>0\) and arbitrarily large \(n\) with \(K(n)\le(1-\varepsilon)k\), monotonicity of \(u\log(n/u)\) on \(0<u\le k<n/e\) would give \(\log M(n)\le(1-\varepsilon+o(1))\sqrt{n\log n}\), contradicting Step 4. Thus \(K(n)/k\to1\). The already established \(k-L\le2\) gives \(L/k\to1\) as well.

## Verification
The crucial extension of [3] is *not* the unsupported assertion that any near-equal triple is distinct: it is the explicit choice of different admissible prime residue classes modulo seven in the **published residue-uniform proof**. Checking all seven residue sums is elementary and complete. The bundled `verify.py` checks exact finite prime partitions and primorial bounds for \(n\le2000\) as a sanity check; the asymptotic assertions are established analytically, not computationally. The source [3] is used at the precise point its residue-uniform argument is required.

## Relationship to prior work
Dong–Robles–Zaharescu–Zeindler [1] establish counting asymptotics for prime-based partitions, rather than the exact extremal cardinality and product properties here. Deléglise–Nicolas [2] treat the relaxed **bounded-sum** maximum and provide the primorial envelope, but do not classify exact-sum completions. Matomäki–Maynard–Shao [3] prove near-equal ternary prime representations without requiring pairwise distinctness in their main theorem; their residue-class-uniform proof allows distinctness to be imposed as above. The **application** giving an eventual two-part deficit, sharp classification on one parity branch, and a polynomial prime-product relaxation ratio is not stated in those primary sources. Campbell [4] proves the unboundedness of a different absolute discrepancy \(L(n)-K(n)\); this is logically compatible with our constant bound on \(k(n)-L(n)\).

## Limitations
The sufficient-size threshold is extremely large and not computed. No optimality is claimed for the constants two and six in the global inequalities. The other parity branch is not completely classified; it may have deficits zero, one or two. The key near-equal representation input is a deep published analytic theorem; the proof is conditional on its established result, **not** on an unproved conjecture. An earlier general additive-completion theorem may already imply the conclusions, so novelty requires independent checking. Small-integer behavior is not covered by the asymptotic theorem.

## References
[1] A. Dong, N. Robles, A. Zaharescu, D. Zeindler, *Strange and pseudo-differentiable functions with applications to prime partitions*, arXiv:2412.20102 (first posted 2024-12-28), Theorems 1.1–1.2.

[2] M. Deléglise and J.-L. Nicolas, *On the Largest Product of Primes with Bounded Sum*, Journal of Integer Sequences 18 (2015), Article 15.2.8, Proposition 1 and Theorem 2, https://cs.uwaterloo.ca/journals/JIS/VOL18/Deleglise/deleglise3.pdf.

[3] K. Matomäki, J. Maynard, X. Shao, *Vinogradov’s theorem with almost equal summands*, Proc. London Math. Soc. 115 (2017), 323–347, arXiv:1610.02017, Theorem 1.1 and proof of Theorem 2.1 (especially §3).

[4] J. M. Campbell, *On a problem on partitions into distinct primes*, arXiv:2610.19534 (2026), Theorem 1, https://arxiv.org/html/2610.19534v1.
