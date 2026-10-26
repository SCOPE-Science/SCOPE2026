# The golden-integer spectrum of first-order limits for Fibonacci-admissible words

## Finding
Let \(W_n\) be uniform over all binary words of length \(n\ge1\) containing no adjacent pair `11`. Regard such a word as the structure on positions \(\{1,\dots,n\}\) with its directed immediate-successor relation \(S(i,j)\iff j=i+1\) and one unary predicate \(P(i)\iff\) the symbol at \(i\) is `1`. There is no full order relation, no arithmetic, and no additional predicates.

Put \(\varphi=(1+\sqrt5)/2\) and \(\mathbb Z[\varphi]=\{a+b\varphi:a,b\in\mathbb Z\}\). The **complete set** of limits of probabilities of first-order sentences in \(\{S,P\}\) is
\[
\mathcal L=\mathbb Z[\varphi]\cap[0,1].
\]
Every fixed first-order sentence has an effectively computable limit, approached at an exponential rate depending on the sentence. Conversely every number in the displayed set is realized by a sentence asserting membership of the word's first bounded-length prefix in an explicit finite set. Hence \(\mathcal L\) is dense in \([0,1]\), but its only rational elements are \(0\) and \(1\). For instance the limit of the sentence saying that the initial position satisfies \(P\) is \(\varphi^{-2}=2-\varphi\).

## Assumptions and scope
Words are sampled uniformly **among the admissible words of each exact length**, not from the stationary infinite Fibonacci word and not from the deterministic Fibonacci substitution sequence. The first-order language contains the successor relation, unary letter predicate, and equality; there is no quantification over sets, order predicate, modulo-counting, or auxiliary constants. Statements are for fixed sentences as \(n\to\infty\). The empty word is excluded but does not affect the limits. The primary mathematical subject is finite-model-theoretic logical convergence (MSC2020 03C13).

Define Fibonacci integers by \(F_0=0\), \(F_1=1\), and \(F_{k+2}=F_{k+1}+F_k\). There are \(F_{n+2}\) admissible words of length \(n\). The notion of probability spectrum used here is a set of **limiting truth probabilities**, not the model-size spectrum of a single sentence.

## Proof
**1. One-ended cylinder probabilities.** Let \(u\) be any admissible word of length \(k\ge1\). The number of length-\(n\) admissible words starting in \(u\), for \(n\ge k\), is \(F_{n-k+2}\) when the last symbol of \(u\) is `0`, and \(F_{n-k+1}\) when its last symbol is `1`. Divide by \(F_{n+2}\) and use Binet's formula. The limiting probability of this prefix is exactly
\[
 c(u)=\begin{cases}\varphi^{-k},&u\text{ ends in `0`},\\
 \varphi^{-(k+1)},&u\text{ ends in `1`}.\end{cases}
\]
By reversing words, the same rule holds for a suffix, now indexed by its **first** symbol. All these probabilities belong to \(\mathbb Z[\varphi]\), because \(\varphi^{-1}=\varphi-1\).

Let \(A=\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\). It is a primitive symmetric matrix, with simple Perron eigenvalue \(\varphi\), other eigenvalue \(-\varphi^{-1}\), and positive Perron vector \((\varphi,1)\). For any fixed admissible prefix \(u\) and suffix \(v\), the number of words of length \(n\) beginning with \(u\) and ending with \(v\) equals the corresponding matrix entry of \(A^{n-|u|-|v|+1}\). Perron decomposition shows that the **two ends become independent**:
\[
 \lim_{n\to\infty}\Pr(W_n\text{ begins with }u\text{ and ends with }v)=c(u)c(v).
\]
The error for fixed \(u,v\) decays exponentially in \(n\).

**2. Interior-pattern saturation.** Fix any finite legal binary word \(v\). For each current predecessor symbol `0` or `1`, a block of length \(|v|+2\) can be prescribed as `0` followed by \(v\) followed by `0`, and this is always admissible. Under the uniform distribution on length-\(n\) admissible words, every allowed next-symbol choice has conditional probability at least \(1/3\), regardless of the already exposed prefix or the remaining length (the values follow from ratios of consecutive Fibonacci numbers). Therefore, at each of \(\lfloor n/(|v|+2)\rfloor\) disjoint blocks, conditional on all earlier blocks, the chosen block contains \(v\) with probability at least \(3^{-(|v|+2)}\). A conditional Chernoff bound implies that, for any fixed threshold \(t\), the probability that \(v\) occurs at fewer than \(t\) of these blocks is at most \(C_{v,t}\exp(-c_v n)\), for positive constants depending only on \(v,t\). This applies simultaneously to every legal word of any fixed bounded length, by a finite union bound.

**3. First-order locality and reduction to the two ends.** Fix a first-order sentence \(\theta\). Effective bounded-degree Hanf locality supplies computable integers \(r,t\) such that its truth is determined by the counts of rooted radius-\(r\) neighborhood types, with counts truncated at \(t\). The Gaifman graph of a coloured successor path has maximum degree two. Every interior radius-\(r\) type corresponds to a legal word of length \(2r+1\), and all these types have counts at least \(t\) with probability \(1-O_\theta(e^{-c_\theta n})\) by step 2. The noninterior neighborhood types and their bounded counts are determined by the first and last \(2r+1\) symbols for sufficiently large \(n\). It follows that one can effectively construct a finite Boolean function \(b_\theta(u,v)\) on admissible prefix/suffix pairs of one fixed length \(h=2r+1\), such that \(\theta\) agrees with \(b_\theta\) outside an exponentially small exceptional event. For an effective construction, enumerate the finite endpoint pairs, build a long legal connecting segment containing each legal length-\(2r+1\) pattern at least \(t\) times, and evaluate \(\theta\) on the resulting finite structure; locality proves that the answer is independent of the connecting segment once it is saturated. Primitivity of \(A\) permits connecting every endpoint pair.

Hence
\[
 \lim_{n\to\infty}\Pr(W_n\models\theta)
 =\sum_{\substack{u,v\text{ admissible of length }h\\ b_\theta(u,v)=1}}c(u)c(v).
\]
This is an effective finite sum of integral powers of \(\varphi^{-1}\), so is in \(\mathbb Z[\varphi]\cap[0,1]\). The two exponential errors in steps 1 and 2 give the claimed convergence rate.

**4. Realizing every algebraic integer in the interval.** Let \(\alpha=m+d\varphi\in\mathbb Z[\varphi]\), with \(0<\alpha<1\), and put \(\psi=(1-\sqrt5)/2=-\varphi^{-1}\) and \(\alpha'=m+d\psi\). For every \(k\ge1\), the identity \(\varphi^2=\varphi+1\) yields unique integers \(a_k,b_k\) satisfying
\[
 \alpha\varphi^{k+1}=a_k\varphi+b_k.
\]
Conjugating and solving the two linear equations gives
\[
 a_k=\frac{\alpha\varphi^{k+1}-\alpha'\psi^{k+1}}{\sqrt5},
 \qquad b_k=a_{k-1}.
\]
By Binet's formula,
\[
 \frac{a_k}{F_{k+1}}\longrightarrow\alpha,
 \qquad \frac{b_k}{F_k}\longrightarrow\alpha.
\]
Because \(0<\alpha<1\), for all sufficiently large \(k\) the integers obey \(0\le a_k\le F_{k+1}\) and \(0\le b_k\le F_k\). There are exactly \(F_{k+1}\) length-\(k\) admissible words ending in `0` and \(F_k\) ending in `1`. Choose any \(a_k\) of the former and any \(b_k\) of the latter. The first-order sentence asserting that the initial \(k\) symbols belong to this selected finite collection has limiting truth probability
\[
 a_k\varphi^{-k}+b_k\varphi^{-(k+1)}=\alpha.
\]
Such a \(k\), and the selected words, are computable by iterating the integer recurrence \((a_{k+1},b_{k+1})=(a_k+b_k,a_k)\) from \((a_0,b_0)=(m+d,d)\). The values \(0\) and \(1\) arise from contradictions and tautologies. This proves the reverse inclusion and the spectrum equality.

Finally, \(\mathbb Z[\varphi]\cap\mathbb Q=\mathbb Z\), since \(\varphi\) is irrational. Thus no nontrivial rational limiting probability is possible. Density follows from the density modulo one of \(\{j\varphi:j\in\mathbb Z\}\), or directly from the preceding realization together with irrational rotation.

## Verification
A standalone pure-Python finite checker, `verify.py`, enumerates all admissible words through length 13, verifies Fibonacci totals and all exact one-ended cylinder counts through prefix length six, compares exact two-ended cylinder counts to transfer-matrix powers, and checks constructive integer prefix representations for small elements of \(\mathbb Z[\varphi]\cap(0,1)\). Executing the embedded program produces `GOLDEN_FO_EXACT_OK 721 19`. All finite computations are checks of identities used in the proof, not substitutes for the Hanf-locality and asymptotic arguments.

## Relationship to prior work
Marström and Räty (2026) establish logical limit laws for small permutation classes by encoding them into regular languages, and explicitly discuss possible extensions to random regular-language words. Their work motivates seeking an **exact arithmetic set** of probabilities in a concrete regular constraint language but does not state the Fibonacci-admissible-word spectrum. Effective bounded-degree Hanf locality is prior mathematics (Kuske and Schweikardt, 2017) and is used, not claimed as new. Standard Fibonacci enumeration and Perron eigenvectors are also prior. Earlier results for uniformly sampled proper ternary successor colourings concern a different transition matrix and rational spectra; they do not imply the irrational golden-integer realization statement. No general claim that this is the first possible appearance of an irrational first-order probability is made.

## Limitations
The theorem is restricted to ordinary first-order logic of **directed successor** and one colour predicate, with uniformly sampled binary words forbidden from containing `11`. It is not about a full linear order, the deterministic Fibonacci substitution word, an MSO language, or arbitrary regular languages. The proof does not give a uniform exponential rate over all sentences. An unlocated general theorem about the measure range of clopen subsets of finite-type shifts combined with first-order locality could subsume the arithmetic spectrum; historical-priority completeness has not been independently verified.

## References
1. K. Marström and E. Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages*, arXiv:2610.22218 (first public version 2026-10-15), https://arxiv.org/abs/2610.22218.
2. D. Kuske and N. Schweikardt, *First-Order Logic with Counting: At Least, Weak Hanf Normal Forms Always Exist and Can Be Computed!*, arXiv:1703.01122 (2017), https://arxiv.org/abs/1703.01122.
3. L. Libkin, *On the Forms of Locality over Finite Models*, LICS (1997), https://www.lfcs.inf.ed.ac.uk/events/lics/1997/Libkin-OntheFormsofLocalit.html.
