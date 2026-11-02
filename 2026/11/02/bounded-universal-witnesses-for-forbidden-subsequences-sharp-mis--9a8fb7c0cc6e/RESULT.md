# Bounded universal witnesses for forbidden subsequences, sharp missing-spectrum jumps and unary optimal hosts

## Finding

Let \(\Sigma\) be a labeled alphabet of cardinality \(q\ge2\), let \(v\in\Sigma^m\) with \(m\ge1\), and let \(K\ge0\). There is an explicitly constructible word \(H_K(v)\) such that, for every \(x\in\Sigma^{\le K}\),
\[
x\preceq H_K(v)\quad\Longleftrightarrow\quad v\not\preceq x.
\]
Here \(\preceq\) means scattered-subsequence containment. The host itself avoids \(v\), and one may take
\[
|H_K(v)|=m(q-1)K+m-1.
\]
Consequently a word missing at least one length-\((k-1)\) subsequence (\(k\ge2\)) must miss at least \((q-1)k+1\) distinct length-\(k\) subsequences. This bound is attained for **every** forbidden \(v\in\Sigma^{k-1}\), with its entire missing length-\(k\) spectrum exactly the one-letter insertion sphere of \(v\).

For the unary forbidden pattern \(v=a^m\) and \(K\ge m\), the **shortest** avoiding host that contains every avoiding length-\(K\) word has length
\[
\boxed{m(q-1)(K-m+1)+m-1}.
\]
The same host therefore contains every shorter avoiding word.

## Assumptions and scope

The finite alphabet has at least two distinct letters. All words are finite and ordered. A subsequence is obtained by deleting zero or more positions without changing their relative order. Avoidance concerns scattered subsequences, **not** contiguous-factor avoidance. Write \(\Sigma^{\le K}=\bigcup_{j=0}^{K}\Sigma^j\). A host is required to avoid the forbidden pattern itself. The word \(v\) may have repeated or adjacent-equal letters. For the unary optimum, \(K\ge m\); no optimal-length assertion is made for other forbidden patterns.

## Proof

**1. A bounded universal host for a principal avoidance class.** Write \(v=v_1\cdots v_m\). For each \(1\le i\le m\), fix an ordering \(\pi_i\) of the \(q-1\) symbols of \(\Sigma\setminus\{v_i\}\). Define
\[
H_K(v)=\pi_1^K v_1\pi_2^K v_2\cdots\pi_{m-1}^K v_{m-1}\pi_m^K.
\]
The degenerate case \(m=1\) has no displayed separator. There are \(m\) permutation blocks and \(m-1\) separators, establishing the length formula.

Apply greedy left-to-right subsequence matching for \(v\). The first block contains no \(v_1\), the next block contains no \(v_2\), and so on. A separator \(v_i\) can advance the greedy match by exactly one letter; within the following block matching cannot advance at all. Thus, after the last block the greedy match has length at most \(m-1\), proving \(v\not\preceq H_K(v)\).

Conversely let \(x\in\Sigma^{\le K}\) avoid \(v\). Run greedy matching for \(v\) inside \(x\), obtaining the unique factorization
\[
x=\alpha_0 v_1\alpha_1 v_2\cdots v_j\alpha_j,
\qquad 0\le j<m,
\]
where each \(\alpha_i\) contains no occurrence of \(v_{i+1}\). A repeated permutation of a finite alphabet \(K\) times contains every word of length at most \(K\) over that alphabet as a subsequence: assign consecutive target letters to successive copies. Each \(\alpha_i\), of length at most \(K\), therefore embeds in \(\pi_{i+1}^K\). Insert the matching separators to embed \(x\) in \(H_K(v)\). If \(K=0\), all blocks are empty, and the same argument covers the empty target word. Combining the two directions gives the claimed equivalence.

**2. Sharp defect jump.** For a word \(v\) of length \(k-1\), let \(I(v)\) be the set of length-\(k\) words formed by inserting one symbol of \(\Sigma\) into any of the \(k\) gaps of \(v\). Every word in \(I(v)\) has \(v\) as a subsequence. There are exactly
\[
|I(v)|=(q-1)k+1
\]
distinct insertions. To see this, fix a symbol \(c\in\Sigma\). Inserting \(c\) at any one of the \(k\) gaps in \(v\) gives two identical words exactly when the insertion locations can be moved across a consecutive run of \(c\)'s. The number of distinct results with inserted symbol \(c\) is therefore \(k-|v|_c\): one representative is the first gap and one for each of the other gaps whose immediately preceding letter is not \(c\). Results for different inserted symbols cannot coincide because the resulting Parikh count identifies the inserted letter uniquely. Summing over \(c\) yields \(qk-\sum_c|v|_c=qk-(k-1)\).

If \(v\not\preceq w\), then \(I(v)\cap\operatorname{Subseq}_k(w)=\varnothing\). Taking \(w=H_k(v)\), part 1 implies that a length-\(k\) word is absent exactly if it contains \(v\) as a subsequence. Since \(|v|=k-1\), this means it belongs to \(I(v)\). The bound is therefore attained with the whole absent spectrum specified.

**3. Exact shortest unary host.** Set \(v=a^m\) and \(t=K-m+1\ge1\). A word avoiding \(a^m\) has at most \(m-1\) occurrences of \(a\). Since it must contain words with \(m-1\) occurrences of \(a\), any feasible host has exactly \(m-1\). Write it uniquely as
\[
G_0 a G_1 a\cdots a G_{m-1},\qquad G_i\in(\Sigma\setminus\{a\})^*.
\]
For each \(i\), every word \(a^i y a^{m-1-i}\) with \(y\in(\Sigma\setminus\{a\})^t\) has length \(K\), avoids \(a^m\), and must embed in the host. Its \(m-1\) occurrences of \(a\) must use all host copies, forcing \(y\preceq G_i\). In particular \(G_i\) must contain \(t\) copies of every non-\(a\) symbol (take \(y=c^t\)); hence \(|G_i|\ge(q-1)t\). This proves the lower bound \(m(q-1)t+m-1\).

Fix a permutation \(\pi\) of the non-\(a\) alphabet and consider
\[
U=(\pi^t a)^{m-1}\pi^t.
\]
Clearly \(U\) avoids \(a^m\) and has the lower-bound length. Let \(x=y_0 a y_1\cdots a y_j\) be any length-\(K\) word avoiding \(a^m\), with \(j\le m-1\) and each \(y_i\) containing no \(a\). Assign \(c_i=\max\{1,\lceil |y_i|/t\rceil\}\) consecutive \(\pi^t\) blocks to its \(i\)-th non-\(a\) run, choosing the intervening \(a\)'s of \(U\) as its \(j\) separators. The total non-\(a\) length \(R=\sum |y_i|\) obeys \(R\le K-j=t+m-1-j\). If \(R=0\), the \(j+1\le m\) blocks suffice. Otherwise
\[
\sum_{i=0}^{j} c_i
= j+1+\sum_{|y_i|>0}\left\lfloor\frac{|y_i|-1}{t}\right\rfloor
\le j+1+\left\lfloor\frac{R-1}{t}\right\rfloor
\le m.
\]
The final inequality follows by setting \(s=m-1-j\ge0\), since \(\lfloor(t+s-1)/t\rfloor\le s\) for \(t\ge1\). Each \(c_i\)-block group is a \((c_i t)\)-universal subsequence host on the non-\(a\) alphabet. Thus \(x\preceq U\). The same construction handles all shorter targets (or pads each target with non-\(a\) letters to length \(K\)). Equality follows.

## Verification

Execute the standalone standard-library checker using `python3 verify.py`. It compares literal subsequence spectra with the construction for bounded alphabets and forbidden patterns, checks insertion-sphere cardinalities, and independently exhausts every shorter candidate unary host in nine small parameter cases. The checker reports `VERIFY_OK principal_instances=407 insertion_spheres=153 unary_exact_optima=9`. These are finite checks; the quantified results follow from the proof, not from finite enumeration.

## Relationship to prior work

Fleischmann, Haschke, Huch, Mayrock and Nowotka (2022), *m-Nearly k-Universal Words — Investigating Simon Congruence*, investigate absent length-\(k\) scattered factors and construct minimal words omitting exactly one specified length-\(k\) factor (Theorem 3.3). Their Theorem 4.1 includes a lower-bound observation for words missing shorter factors. These facts are acknowledged. The present result instead gives an explicit host with the entire spectrum of words avoiding an arbitrary shorter forbidden subsequence, a sharp all-alphabet insertion-sphere defect jump, and an exact extremal cost for every unary forbidden pattern. Adamson et al. (2023) investigate universality inside regular languages; the forbidden-pattern relative host and unary extremum are different statements. Classical Higman–Haines subword-ideal theory provides related general background, which may imply parts of the cofinality claim abstractly; the finite exact costs and sharp spectrum are the emphasized contributions.

## Limitations

No claim is made about the shortest host for arbitrary nonunary forbidden patterns, or about all possible missing spectra for every nearly universal word. The standalone exhaustive calculations cover finite cases only. A mathematically equivalent formulation may occur in classical subword ideal or shortest common supersequence literature not located by the comparison searches; independent scholarly review has not been performed.

## References

1. P. Fleischmann, L. Haschke, A. Huch, A. Mayrock, D. Nowotka, *m-Nearly k-Universal Words — Investigating Simon Congruence*, arXiv:2202.07981v1 (public 2022-02-16), https://arxiv.org/html/2202.07981v1.
2. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658 (first public 2023-11-17), https://arxiv.org/abs/2311.10658.
3. A. Okhotin, *On the State Complexity of Scattered Substrings and Superstrings*, Fundamenta Informaticae 99 (2010), 325–338, https://doi.org/10.3233/FI-2010-252 (abstract consulted; full text not inspected).
