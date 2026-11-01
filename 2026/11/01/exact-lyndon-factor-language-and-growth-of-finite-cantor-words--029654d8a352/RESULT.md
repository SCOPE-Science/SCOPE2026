# Exact Lyndon-factor language and growth of finite Cantor words

## Finding
Let \(C_0=1\), and for every integer \(n\ge 1\) let \(C_n=C_{n-1}0^{3^{n-1}}C_{n-1}\). All words are binary with order \(0<1\), and \(\mathcal L_n\) denotes the set of **distinct nonempty contiguous Lyndon factors** of \(C_n\). Then \(\mathcal L_0=\{1\}\), \(\mathcal L_1=\{0,1,01\}\), and for every integer \(n\ge2\) there is a disjoint language decomposition
\[
\mathcal L_n=\mathcal L_{n-1}\;\sqcup\;
\left\{0^t u:\ 3^{n-2}<t\le3^{n-1},\quad
u\text{ is a nonempty prefix of }C_{n-1}\text{ ending in }1\right\}.
\]
In particular, the new factors at rank \(n\) number exactly \(4\cdot 6^{n-2}\). Hence
\[
\boxed{|\mathcal L_n|=\frac{4\cdot6^{n-1}+11}{5}\qquad(n\ge1).}
\]
Equivalently, if \(N=|C_n|=3^n\), the total grows on the exact scale \(N^{\log_3 6}\), with asymptotic coefficient \(2/15\).

The decomposition also determines every length-specific count. Let \(\lambda_n(\ell)\) count members of \(\mathcal L_n\) of length \(\ell\), and write \(f(j)=2\sum_{r\ge0}\epsilon_r(j)3^r\), where \(\epsilon_r(j)\in\{0,1\}\) are binary digits. The one-positions of \(C_{n-1}\), zero indexed, are exactly \(f(j)\) for \(0\le j<2^{n-1}\). Thus for \(n\ge2\),
\[
\lambda_n(\ell)-\lambda_{n-1}(\ell)=
\#\bigl\{j\in[0,2^{n-1}-1]:\ 3^{n-2}<\ell-f(j)-1\le3^{n-1}\bigr\}.
\]

## Assumptions and scope
A Lyndon word is a nonempty primitive word lexicographically smaller than every nontrivial rotation; equivalently, it is strictly smaller than each proper nonempty suffix. The shorter of two comparable prefix strings is lexicographically smaller. All occurrences are **linear contiguous** factors; factors are counted as distinct strings, not by multiplicity. Each \(C_n\) has length \(3^n\), begins and ends with \(1\), contains \(2^n\) ones, and has longest run of zeros \(3^{n-1}\) when \(n\ge1\). The claimed recursion starts at \(n=2\); the base ranks are stated separately.

## Proof
**Binary endpoint observation.** Every binary Lyndon word of length at least two starts with \(0\) and ends with \(1\). If it starts with \(1\) and contains \(0\), a suffix beginning at \(0\) is smaller; a constant word of length greater than one is not primitive. If it starts with \(0\) and ends with \(0\), the one-letter suffix \(0\) is smaller than the full word. This proves the observation.

**Base case.** Direct inspection of \(C_1=101\) gives \(\mathcal L_1=\{0,1,01\}\).

**Inductive boundary analysis.** Fix \(n\ge2\), and put \(U=C_{n-1}\), \(V=C_{n-2}\), \(G=3^{n-1}\), and \(g=3^{n-2}\). Then \(C_n=U0^G U\), \(U=V0^g V\), and every zero-run inside \(U\) has length at most \(g\). Every Lyndon factor contained in either copy of \(U\) already lies in \(\mathcal L_{n-1}\). Consider a further Lyndon factor crossing the central run \(0^G\). By the endpoint observation it ends at a \(1\) in the right copy of \(U\).

If it begins in the left copy of \(U\), its initial zero-run has length at most \(g<G\), whereas it contains the complete central run \(0^G\). A proper suffix starting at that central run is smaller than the factor, contradicting its Lyndon property. Hence any additional Lyndon factor starts inside the central run and is exactly \(0^t u\), with \(1\le t\le G\) and \(u\) a prefix of \(U\) ending in \(1\).

If \(g<t\le G\), the initial zero-run is strictly longer than every later zero-run in \(u\). Every proper suffix therefore starts either at \(1\) or at a zero-run shorter than \(t\), and is lexicographically larger. Thus \(0^tu\) is Lyndon. It is absent from \(U\) because \(U\) has no zero-run longer than \(g\).

It remains to exclude new Lyndon strings when \(t\le g\). If \(u\) ends in the first copy of \(V\) in \(U=V0^gV\), then \(0^tu\) already occurs in \(U\), by taking the last \(t\) zeros of its middle run and the same prefix of the second \(V\). Otherwise \(u=V0^g u'\), where \(u'\) is a nonempty prefix of \(V\) ending in \(1\). For \(t<g\), the proper suffix \(0^g u'\) is smaller than \(0^tV0^gu'\). For \(t=g\), this proper suffix is a strict prefix of \(0^gV0^gu'\), and is again smaller. Either way the candidate cannot be Lyndon. This proves the exact disjoint language decomposition.

**Counting.** The \(2^{n-1}\) occurrences of \(1\) in \(U\) determine exactly \(2^{n-1}\) distinct nonempty prefixes ending in \(1\). There are \(G-g=2\cdot3^{n-2}\) available values of \(t\). Pairs \((t,u)\) produce distinct strings, since \(t\) is their leading zero-run length and \(u\) is then determined. Thus
\[
|\mathcal L_n|-|\mathcal L_{n-1}|=(2\cdot3^{n-2})2^{n-1}=4\cdot6^{n-2}.
\]
Together with \(|\mathcal L_1|=3\), summing the geometric progression gives the displayed formula. A \(1\) in \(C_{n-1}\) is located precisely at \(f(j)\), by induction on the self-similar two-copy construction, so the prefix ending there has length \(f(j)+1\). Each new factor \(0^tu\) has length \(t+f(j)+1\), proving the length-specific formula.

## Verification
Run `python3 checker.py`. The independent finite procedure constructs all distinct factors of each \(C_n\) for ranks \(0\) through \(5\), tests the lexicographic proper-suffix characterization, independently constructs the predicted rank decomposition, and requires **equality of complete sets**, not merely matching totals. Results: ranks \(0,1,2,3,4,5\) give \(1,3,7,31,175,1039\) distinct Lyndon factors, with all set comparisons passing. The checker is finite evidence only; the unrestricted claim follows from the inductive proof.

## Relationship to prior work
Saari's study of Lyndon words and Fibonacci numbers establishes lower bounds and structural results for Lyndon factors of Fibonacci and recurrent words. Goc, Saari and Shallit establish automaticity and regularity properties for Lyndon complexity in automatic sequences. Glen, Simpson and Smyth obtain general extremal and average counts and detailed results for Christoffel and Sturmian words. These do not state the threshold decomposition for the finite Cantor iterates or its explicit rank-count formula. In particular, knowing that the lengthwise Lyndon complexity of a \(3\)-automatic infinite word is \(3\)-regular does not itself specify which distinct factors occur in a finite iterate. The present proof uses the unique new longest zero-run at each iteration to classify the exact addition of factors.

## Limitations
The theorem is for the binary Cantor substitution \(1\mapsto101\), \(0\mapsto000\), complete iterates, fixed order \(0<1\), distinct **linear** factors, and no multiplicity weighting. It does not apply unchanged to circular factors, arbitrary prefixes, reversed alphabet order, other Cantor-like morphisms, or factor-occurrence counts. The finite checker is not a proof for unbounded rank. Full historical priority has not been established; related work in other descriptions or repositories may exist.

## References
1. K. Saari, *Lyndon words and Fibonacci numbers*, arXiv:1207.4233 (first posted 2012-07-17), https://arxiv.org/abs/1207.4233.
2. D. Goc, K. Saari and J. Shallit, *Primitive Words and Lyndon Words in Automatic and Linearly Recurrent Sequences*, arXiv:1207.5124 (first posted 2012-07-21), https://arxiv.org/abs/1207.5124.
3. A. Glen, J. Simpson and W. F. Smyth, *Counting Lyndon factors*, arXiv:1701.00928 (first posted 2017-01-04), https://arxiv.org/abs/1701.00928.
