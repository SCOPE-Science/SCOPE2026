# Thue–Morse shortest-absent-subsequence counts from a binary morphism duality

## Finding

Let \(\Sigma=\{0,1\}\), and let \(\mu:\Sigma^*\to\Sigma^*\) be the uniform morphism \(\mu(0)=01\), \(\mu(1)=10\). For a word \(w\), let \(\operatorname{SAS}(w)\) denote the set of *shortest absent subsequences*: words not obtainable from \(w\) by deleting letters without reordering, with shortest possible length. Let \(D(v)\) count the **distinct** subsequences of \(v\), including the empty word.

**Morphism duality and Thue–Morse theorem.** For every binary word \(v=v_1\cdots v_m\) with \(m\ge1\), the shortest absent subsequences of \(\mu(v)\) all have length \(m+1\), and
\[
\operatorname{SAS}(\mu(v))
=\{x_1\cdots x_{m+1}\in\Sigma^{m+1}: (x_i,x_{i+1})\ne(v_i,1-v_i)\text{ for all }1\le i\le m\},
\qquad |\operatorname{SAS}(\mu(v))|=D(v)+1.
\]

For \(T_0=0\) and \(T_{k+1}=\mu(T_k)\), define integers \(t_0=1\), \(t_1=2\) and, for \(k\ge0\),
\[
t_{k+2}=t_{k+1}(t_k^2+2).
\]
Then for **every** \(k\ge0\),
\[
\boxed{|\operatorname{SAS}(T_{k+1})|=t_k+t_{k-1}^{\,2}+2}\qquad(k\ge1),
\quad |\operatorname{SAS}(T_1)|=3.
\]
Equivalently, writing \(s_{k+1}=|\operatorname{SAS}(T_{k+1})|\), one has \(s_{k+1}=t_k+a_k\), where \(a_0=2\) and \(a_k=t_{k-1}^2+2\) for \(k\ge1\). The first values of \(s_{k+1}\), starting at \(k=0\), are
\[
3,\quad5,\quad12,\quad74,\quad2666,\quad3647090,\quad6476006417762.
\]
In particular, for the natural scaling by \(2^k\), an exact exponential growth base exists:
\[
\lim_{k\to\infty} s_{k+1}^{1/2^k}=\rho,
\quad
\rho=\exp\!\left(\frac{\log 2}{3}+\frac13\sum_{j=0}^{\infty}2^{-j-1}\log\!\left(1+\frac{2}{t_j^2}\right)\right)
=1.56866478915\ldots .
\]
The sum converges absolutely. The result determines *cardinalities* of shortest absent scattered words for all finite dyadic Thue–Morse iterates, rather than the occurrence multiplicities of ordinary contiguous factors.

## Assumptions and scope

All words are finite and binary, except for the empty subsequence included in \(D(v)\). Subsequence occurrence means indices strictly increasing, not necessarily consecutive; distinct subsequences are counted once, irrespective of how many embeddings exist. The full duality requires nonempty \(v\). The Thue–Morse fixed-point seed is \(T_0=0\); thus \(|T_k|=2^k\), and \(\mu(T_k)=T_{k+1}\). The formula concerns shortest absent subsequences of the **entire finite linear word** \(T_{k+1}\), not arbitrary factors of the infinite fixed point.

## Proof

**Step 1: shortest length and local criterion.** Every block \(\mu(v_i)\) contains both binary symbols exactly once, so each target of length \(m\) can be greedily embedded using one symbol from each of the \(m\) blocks. No binary target of length \(m+1\) is forced to be present: for instance, choose its first bit arbitrarily, and for each \(i\) choose its next bit so that the adjacent pair is not \(\mu(v_i)\); the resulting word cannot be embedded, as proved next.

For any target \(x=x_1\cdots x_{m+1}\), use the leftmost greedy subsequence matching algorithm within \(\mu(v)\). Before the first block in which two target letters are matched, precisely one target letter is matched in each encountered block (unless matching has already finished). Such a first two-letter match occurs in block \(i\) if and only if the next two targets are \((x_i,x_{i+1})=(v_i,1-v_i)\). Once two targets have been matched inside one block, at least \(i+1\) targets have been matched by block \(i\) and one per subsequent block completes all \(m+1\) targets by the end. Conversely, if no block permits a two-letter match, exactly \(m\) letters have been matched after all blocks and the last target is missing. Thus the displayed criterion is necessary and sufficient for absence. This also proves that \(m+1\) is the shortest absent length.

**Step 2: cardinality duality.** For target prefixes satisfying the local avoidance rules after \(i\) steps, let \(p_i\) and \(q_i\) count those ending in \(0\) and \(1\), respectively. Initially \((p_0,q_0)=(1,1)\), corresponding to both possible one-letter target prefixes. On reading \(v_{i+1}=0\), the transition forbids \(01\), hence
\[
(p_{i+1},q_{i+1})=(p_i+q_i,q_i).
\]
On reading \(v_{i+1}=1\), it forbids \(10\), hence
\[
(p_{i+1},q_{i+1})=(p_i,p_i+q_i).
\]
Independently, let \(u_i^{(0)}\) and \(u_i^{(1)}\) count distinct *nonempty* subsequences of the prefix \(v_1\cdots v_i\) ending in \(0\) and \(1\), respectively; initialize both at zero. Appending symbol \(c\) creates precisely the words obtained by concatenating \(c\) to each distinct subsequence of the previous prefix (including the empty one). Consequently \(u_{i+1}^{(c)}=1+u_i^{(0)}+u_i^{(1)}\), while the other endpoint class is unchanged. Therefore induction gives \(p_i=u_i^{(0)}+1\) and \(q_i=u_i^{(1)}+1\). Summing yields
\[
|\operatorname{SAS}(\mu(v))|=p_m+q_m=u_m^{(0)}+u_m^{(1)}+2=D(v)+1.
\]
This equality compares distinct scattered subsequences of a source word with shortest absent scattered subsequences of its complementary-pair image; neither count is the number of embeddings.

**Step 3: exact nonlinear recurrence.** Define
\[
L_0=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
L_1=\begin{pmatrix}1&0\\1&1\end{pmatrix},\quad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
For \(w=w_1\cdots w_r\), put \(M(w)=L_{w_r}\cdots L_{w_1}\) and \(M_k=M(T_k)\). Step 2 gives \(s_{k+1}=\mathbf1^{\mathsf T}M_k\mathbf1\), where \(\mathbf1=(1,1)^{\mathsf T}\). Since \(L_{1-c}=JL_cJ\), complementation gives \(M(\overline{T_k})=JM_kJ\). The defining identity \(T_{k+1}=T_k\overline{T_k}\) implies
\[
M_{k+1}=JM_kJM_k=(JM_k)^2.
\]
Since \(\det M_k=1\) and \(\det J=-1\), Cayley–Hamilton for the two-by-two matrix \(JM_k\) gives
\[
M_{k+1}=I+t_kJM_k,\qquad t_k=\operatorname{tr}(JM_k).
\]
Set \(a_k=\operatorname{tr}(M_k)\). Taking traces yields the **exact**, coupled identities
\[
a_{k+1}=t_k^2+2,\qquad t_{k+1}=a_kt_k,
\qquad (a_0,t_0)=(2,1).
\]
Eliminating \(a_k\) yields \(t_1=2\) and \(t_{k+2}=t_{k+1}(t_k^2+2)\) for all \(k\ge0\). Finally, in two dimensions \(\mathbf1^{\mathsf T}M_k\mathbf1=\operatorname{tr}(M_k)+\operatorname{tr}(JM_k)=a_k+t_k\), proving the displayed integer count.

**Step 4: exact limiting base.** Write \(\ell_k=\log t_k\) and \(b_k=\log(1+2/t_k^2)\). The positive recurrence gives
\[
\ell_{k+2}=\ell_{k+1}+2\ell_k+b_k,
\quad \ell_0=0,\quad\ell_1=\log2.
\]
Solving this inhomogeneous linear recurrence gives, for \(k\ge1\),
\[
\ell_k=\frac{2^k-(-1)^k}{3}\log2
+\frac13\sum_{j=0}^{k-2}\left(2^{k-j-1}-(-1)^{k-j-1}\right)b_j.
\]
Because \(0<b_j\le\log3\), division by \(2^k\) and dominated convergence give the stated finite constant \(C=\lim_{k\to\infty}\ell_k/2^k\). For \(k\ge1\), \(a_k=t_{k-1}^2+2\). Therefore \(\log a_k/2^k\to C\) and \(\log t_k/2^k\to C\). The inequalities \(\max\{a_k,t_k\}\le s_{k+1}\le2\max\{a_k,t_k\}\) imply \(\log s_{k+1}/2^k\to C\), so \(\rho=e^C\). This completes the proof.

## Verification

The standalone `checker.py` compares four **independently implemented** finite calculations for every one of the \(510\) binary source words of lengths \(1\) through \(8\): the forbidden-pair automaton, direct greedy subsequence matching, ordinary distinct-subsequence dynamic programming, and the transfer sum. It also independently verifies the exact matrix recursion and shortest-absent counts for \(T_{k+1}\) with \(0\le k\le8\) (largest host length \(512\)). It prints the exact values and a numerical approximation of \(\rho\).

Execute `python3 checker.py` with Python 3 and no dependencies. The proof covers all lengths regardless of this finite testing; the checker is a falsification aid rather than an exhaustive verification of an infinite theorem. The limit series itself supplies a rigorous convergent specification of the base, and its displayed decimal is an approximation.

## Relationship to prior work

The distinction between non-contiguous subsequence membership and distinct-subsequence counting is classical. Flaxman, Harrow and Sorkin (2004) studied **maximal numbers** of distinct subsequences over words of a fixed length, giving Fibonacci-type extremal counts. Collins (2013) considered expected counts in random binary words. Kosche, Koß, Manea and Siemer (2021) gave general characterizations of shortest absent subsequences through arch factorizations (notably Theorem 3.5) and their concatenation (Lemma 3.16); these general results **cover the abstract existence of a local constraint description** for concatenations of binary permutation blocks. The local forbidden-pair condition is therefore not asserted as independently novel.

The specific bridge \(|\operatorname{SAS}(\mu(v))|=D(v)+1\) for every binary preimage and the nonlinear all-level Thue–Morse recurrence with an explicit limiting exponential base are the distinct claims assessed here. The 2017 paper by Leroy, Rigo and Stipulanti counts scattered subwords of binary and Fibonacci number representations using generalized Pascal triangles; its inspected sections do not analyze Thue–Morse substitution iterates or the shortest-absence bridge. The cited structural and counting results concern different invariants or quantifiers and do not state this exact source-image duality or its Thue–Morse nonlinear recurrence.

## Limitations

The identity assumes the exact complementary-pair morphism and a binary alphabet. It does not extend as stated to arbitrary substitutions or larger alphabets. The nonlinear recurrence concerns finite complete iterates \(T_k\), not length-\(n\) prefixes for arbitrary \(n\), occurrence-weighted subsequences, or general factor complexity. Other presentations of the duality or the dyadic recurrence might exist under equivalent finite-automaton or scattering terminology; exhaustive priority verification was not possible. Numerical tests alone do not establish any of the universal statements.

## References

1. A. Flaxman, A. W. Harrow, G. B. Sorkin, “Strings with maximally many distinct subsequences and substrings,” *Electronic Journal of Combinatorics* 11 (2004), R8, published 2004-01-05. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r8/pdf
2. M. J. Collins, “The Number of Distinct Subsequences of a Random Binary String,” arXiv:1310.7288 (2013). https://arxiv.org/abs/1310.7288
3. M. Kosche, T. Koß, F. Manea, S. Siemer, “Absent Subsequences in Words,” arXiv:2108.13968 (2021), especially §3 and Theorem 3.5. https://arxiv.org/abs/2108.13968
4. J. Leroy, M. Rigo, M. Stipulanti, “Counting the number of non-zero coefficients in rows of generalized Pascal triangles,” *Discrete Mathematics* (2017). https://orbi.uliege.be/bitstream/2268/205077/1/postprint%20auteur.pdf
