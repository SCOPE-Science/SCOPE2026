# Exact enumerative coincidence of Lyndon and Galois rotations at a unique shortest gap

## Finding
Fix the ordered binary alphabet \(0<1\). Let \(\mathcal C_n\) be the set of primitive binary necklaces of length \(n\) having at least two occurrences of \(0\), no cyclic occurrence of \(00\), and a unique shortest cyclic run of \(1\)'s between consecutive zeros. Let \(u_n\) (respectively \(v_n\)) count the necklaces in \(\mathcal C_n\) whose smallest cyclic rotations under ordinary and alternating lexicographic order agree (respectively disagree). Alternating order compares symbols normally in positions \(1,3,5,\ldots\), and in the opposite order in positions \(2,4,6,\ldots\), with positions numbered from one. Then
\[
\sum_{n\ge0}u_nz^n=\sum_{\substack{a\ge1\\a\ \mathrm{odd}}}\frac{z^{2a+3}}{1-z-z^{a+2}},\qquad
\sum_{n\ge0}v_nz^n=\sum_{\substack{a\ge2\\a\ \mathrm{even}}}\frac{z^{2a+3}}{1-z-z^{a+2}}.
\]
Let \(\rho_a\) be the unique root in \((0,1)\) of \(1-z-z^{a+2}=0\), and let \(\lambda_a=1/\rho_a\) and \(c_a=\rho_a^{2a+2}/(1+(a+2)\rho_a^{a+1})\). As \(n\to\infty\),
\[
u_n\sim c_1\lambda_1^n,\quad v_n\sim c_2\lambda_2^n,\quad
\frac{u_n}{u_n+v_n}=1-\frac{c_2}{c_1}\left(\frac{\lambda_2}{\lambda_1}\right)^n(1+o(1)),
\]
where \(\lambda_1=1.465571231876\ldots\) and \(\lambda_2=1.380277569097\ldots\). Thus almost every necklace within \(\mathcal C_n\) has the same two canonical rotations, even though among *all* primitive binary necklaces the coincidence proportion is \(O((\varphi/2)^n)\), where \(\varphi=(1+\sqrt5)/2\). Moreover, the total number of coincident primitive necklaces is at least \(u_n\), giving an exponential lower bound \(\Omega(\lambda_1^n)\).

## Assumptions and scope
A binary necklace is a cyclic-rotation equivalence class of finite words. A primitive necklace has no proper-power representative. If a necklace has no adjacent zeros, it is described cyclically by \(r\ge2\) positive run lengths \((a_1,\ldots,a_r)\) of ones between zeros. We restrict to necklaces in which the smallest such length occurs once, an intrinsic (rotation-invariant) condition. Such necklaces are automatically primitive: a nontrivial power would repeat every gap count, in particular the smallest one. The two canonical rotations are unique because the necklace is primitive. The asymptotics concern \(n\to\infty\) through all integers; at small lengths the counts may be zero.

## Proof
**Parity comparison.** Label the unique smallest one-gap by \(a\). Every rotation starting with \(1\) is greater than every rotation starting with \(0\) under both orders. The rotation beginning at the zero immediately before the unique run \(1^a\) is lexicographically smallest: comparing it with a rotation beginning at any other zero, the first difference is at zero-based position \(a+1\), where the proposed rotation has \(0\) and the other has \(1\). This same comparison is performed normally by alternating order exactly when \(a+1\) is even, i.e. \(a\) is odd. If \(a\) is even, every longer-gap rotation is smaller than the unique shortest-gap rotation in alternating order. Thus the two canonical rotations coincide if and only if \(a\) is odd.

**Rooted cyclic gap counting.** Because the shortest gap is unique, cyclic rotation has a canonical root at that gap. Fix its length \(a\). There are \(k\ge1\) further gaps, each with length \(a+1+t_i\), \(t_i\ge0\). One zero follows each one-run, so the word length is \((a+1)+k(a+2)+\sum_i t_i\). The ordinary generating function, summed over \(k\ge1\), is
\[
\sum_{k\ge1}z^{a+1}\left(\frac{z^{a+2}}{1-z}\right)^k
=\frac{z^{2a+3}}{1-z-z^{a+2}}.
\]
Each necklace is counted exactly once, because the root is intrinsic and the ordered list of remaining gaps is read in the cyclic direction. Splitting \(a\) by parity proves both generating series. Equivalently the coefficient for fixed \(a\) and \(k\) is \(\binom{n-a-1-k(a+2)+k-1}{k-1}\) whenever \(n\ge a+1+k(a+2)\).

**Asymptotics.** For each \(a\), \(\rho_a\) is a simple positive root; it is the only root of least modulus because equality in \(|z+z^{a+2}|\le |z|+|z|^{a+2}\) at the root forces \(z\) to be positive real. Taking the residue yields coefficient \(c_a\lambda_a^n+O(\eta_a^n)\) for some \(\eta_a<\lambda_a\). The roots strictly increase with \(a\), hence \(\lambda_1>\lambda_2>\lambda_3>\cdots>1\). For every \(r\) strictly between \(\rho_2\) and \(\rho_3\), the sum of summands with odd \(a\ge3\) is analytic and normally convergent on \(|z|\le r\); for every \(r\) between \(\rho_2\) and \(\rho_4\), the sum over even \(a\ge4\) is similarly analytic. Cauchy's estimate makes the respective tails exponentially smaller than the \(a=1\) and \(a=2\) terms. This proves the stated equivalents and the ratio.

**Global contrast.** Suppose a primitive binary necklace contains both symbols and has coinciding canonical rotations. If it contained a cyclic \(00\), its ordinary-minimum rotation would begin \(00\), whereas an alternating-minimum rotation would begin \(01\); contradiction. Hence it avoids cyclic \(00\). The number of length-\(n\) binary strings avoiding cyclic \(00\) is the Lucas number \(L_n=\varphi^n+(-\varphi^{-1})^n\). Since a primitive length-\(n\) necklace has exactly \(n\) distinct rooted rotations, the number of coincident necklaces is at most \(L_n/n\). The total number of primitive binary necklaces is \(n^{-1}\sum_{d\mid n}\mu(d)2^{n/d}=2^n/n+O(2^{n/2})\), yielding the stated \(O((\varphi/2)^n)\) upper bound for the coincidence proportion. Every \(\mathcal C_n\) necklace with odd unique shortest gap is a coincident necklace, so the lower bound follows from the first asymptotic.

## Verification
Run `python3 verify.py` with Python 3's standard library. The program independently checks the generating-function coefficient formula against direct enumeration of all binary words of lengths \(1\) through \(18\), tests the canonical-rotation parity implication in both directions, and tests the global cyclic-\(00\) obstruction on primitive words through length \(14\). Its expected marker is `GALOIS_LYNDON_UNIQUE_SHORTEST_PASS`. The infinite claims rest on the preceding proofs rather than on finite enumeration.

## Relationship to prior work
Hendrian–Köppl–Yoshinaka–Shinohara (2024) give algorithms for recognition, factorization, and canonical rotation of Galois words under alternating order. Daykin–Mhaskar–Smyth (2024), especially Lemma 50 and Theorem 54, give stronger general structural information and a factorization characterization of binary border-free Galois words. These results cover general membership testing, so the local parity criterion is not presented as an independent broad characterization of Galois words. The present, narrower contribution is the exact simultaneous-rotation **enumeration**, including its infinite generating functions and opposed conditional/global asymptotics for a natural uniquely rooted cyclic-gap family. No independent audit or complete search of all unindexed literature has been performed.

## Limitations
The generating series do not enumerate all primitive necklaces having coincident canonical rotations; they enumerate only the precisely defined \(\mathcal C_n\) subclass. The global coincidence result is an upper bound, not a sharp asymptotic for all necklaces. The broader binary Galois characterization in the 2024 work is relevant prior coverage and leaves a residual originality risk concerning alternative enumerative derivations. The stated exponential constants and complete member counts are mathematically derived, not independently certified.

## References
- D. Hendrian, D. Köppl, R. Yoshinaka, A. Shinohara, *Algorithms for Galois Words: Detection, Factorization, and Rotation*, arXiv:2403.02636 (first publicly submitted 2024-03-05), https://arxiv.org/abs/2403.02636.
- J. W. Daykin, N. Mhaskar, W. F. Smyth, *V-Words, Lyndon Words and Galois Words*, arXiv:2409.02757 (first publicly submitted 2024-09-04), https://arxiv.org/abs/2409.02757.
- R. Giancarlo et al., *The Alternating BWT: An Algorithmic Perspective*, arXiv:1907.02308, https://arxiv.org/abs/1907.02308.
