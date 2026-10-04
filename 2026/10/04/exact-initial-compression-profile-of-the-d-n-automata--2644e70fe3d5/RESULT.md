# Exact initial compression profile of the \(D'_n\) automata
## Finding
For the Ananichev–Gusev–Volkov automaton \(D'_n\) on \(Q=\{1,\ldots,n\}\), \(n\ge4\), with \(b(i)=i+1\) for \(i<n\), \(b(n)=1\), and \(a(i)=i+1\) for \(1\le i\le n-2\), \(a(n-1)=1\), \(a(n)=2\), define \(\lambda_n(s)=\min\{|w|:|Qw|\le n-s\}\). Put \(h_n=2n/3\) when \(3\mid n\), and \(h_n=\lfloor n/3\rfloor+1\) otherwise. Then for every \(1\le s\le h_n\), \(\lambda_n(s)=3s-2\), and the unique shortest word is \(a(b^2a)^{s-1}\). Moreover \(\lambda_n(h_n+1)>3(h_n+1)-2\).

Thus the shortest linear-rate compression phase lasts for a residue-dependent number of rank drops: \(2n/3\) drops when \(3\mid n\), but only \(\lfloor n/3\rfloor+1\) drops otherwise. At the next target the universal spacing lower bound is no longer attainable.

## Assumptions and scope
The state set is \(Q=\{1,\ldots,n\}\) with \(n\ge4\). The two letters act by
\[
b(i)=\begin{cases}i+1,&i<n,\\1,&i=n,\end{cases}
\qquad
a(i)=\begin{cases}i+1,&1\le i\le n-2,\\1,&i=n-1,\\2,&i=n.\end{cases}
\]
This is the labeling of the coloring \(D'_n\) determined by the digraph \(D_n\): the source proves that \(b\) is a cyclic permutation, that \(a\) merges states \(1\) and \(n\) at state \(2\), and that \(a(n-1)=1\).

For a word \(w\), its image is \(Qw\). A use of \(a\) is called effective when it lowers the current image cardinality. Since \(a\) has exactly one collision pair, \(\{1,n\}\), every effective use lowers cardinality by exactly one.

## Proof
Only the letter \(a\) can lower image cardinality. Immediately after an effective \(a\), state \(n\) is absent because \(n\) is not in the image of \(a\). Therefore the next letter cannot itself be an effective \(a\). If the next letter is \(b\), state \(1\) is absent afterward, because its unique \(b\)-preimage is \(n\). Hence an effective \(a\) cannot occur after only one intervening letter. Consecutive effective occurrences of \(a\) are separated by at least two letters.

Equality in this spacing bound is rigid. Between two consecutive effective occurrences of \(a\), a two-letter gap beginning with \(a\) cannot work: after \(a\) state \(n\) remains absent, while a following \(b\) would instead leave state \(1\) absent. A gap \(ba\) also leaves state \(n\) absent just before the next \(a\). Thus the only two-letter gap that can support equality is \(bb\). To obtain deficiency \(s\), at least \(s\) effective occurrences of \(a\) are required, so
\[
|w|\ge 1+3(s-1)=3s-2.
\]
If equality holds, the first effective \(a\) must be the first letter, every gap must be \(bb\), and the last effective \(a\) must be the final letter. Consequently the only possible equality word is
\[
w_s=a(b^2a)^{s-1}.
\]

It remains to determine for how long this forced word keeps every occurrence of \(a\) effective. Let \(H_s=Q\setminus Qw_s\) be its hole set after the \(s\)-th effective \(a\). We have \(H_1=\{n\}\). Before a subsequent \(a\), the factor \(b^2\) shifts all holes by two cyclic positions. The next \(a\) is effective exactly when both collision preimages \(1\) and \(n\) are present, equivalently when \(H_s\cap\{n-2,n-1\}=\varnothing\). Under this condition,
\[
H_{s+1}=\{n\}\cup F(H_s),
\]
where, on the values encountered before failure,
\[
F(n)=3,\qquad F(n-3)=1,\qquad F(j)=j+3\quad(1\le j\le n-4).
\]
The map \(F\) is injective there and never takes the value \(n\), so
\[
H_s=\{n,F(n),F^2(n),\ldots,F^{s-1}(n)\}.
\]

Write \(n=3m+r\), with \(r\in\{0,1,2\}\). If \(r=0\), the orbit beginning at \(n\) is
\[
n,3,6,\ldots,n-3,1,4,7,\ldots,n-2,
\]
and the first forbidden hole \(n-2\) enters at the \(2m\)-th hole set. Hence \(w_s\) has deficiency exactly \(s\) for \(s\le2m=2n/3\), while the next forced equality word fails to gain another rank drop. If \(r=1\), the orbit starts
\[
n,3,6,\ldots,3m=n-1,
\]
so the first forbidden hole appears at \(s=m+1\). If \(r=2\), it starts
\[
n,3,6,\ldots,3m=n-2,
\]
with the same stopping index \(s=m+1\). These are exactly the stated values of \(h_n\).

Therefore \(w_s\) attains the lower bound for every \(1\le s\le h_n\), proving \(\lambda_n(s)=3s-2\) and uniqueness. At \(s=h_n+1\), any word of length \(3s-2\) would have to be the same forced word, but its final \(a\) is ineffective because the preceding hole set already contains \(n-2\) or \(n-1\). Hence \(\lambda_n(h_n+1)>3(h_n+1)-2\).

## Verification
A standalone verifier exhaustively runs the full power automaton for every \(4\le n\le18\). For each \(1\le s\le h_n\) it checks the shortest attainable length, counts all shortest words, and confirms both \(\lambda_n(s)=3s-2\) and uniqueness. It also checks strict failure at \(h_n+1\). A second direct replay checks the witness deficiency and the saturation boundary for every \(4\le n\le300\). The packaged verifier prints `VERIFY_OK`.

## Relationship to prior work
Ananichev, Gusev, and Volkov introduced the \(D'_n\) coloring in the 2010 preprint and proved its reset length \(n^2-3n+4\), giving the reset word \((ab^{n-2})^{n-2}ba\). The same-family 2013 extended treatment again proves that reset threshold and describes \(D'_n\) as an extremal slowly synchronizing family. The inspected texts do not state a minimum-length function for intermediate image cardinalities, the unique words \(a(b^2a)^{s-1}\), or the residue-class boundary \(h_n\). Their full text also contains no occurrence of the term “rank” in this automata sense.

The present statement is not implied by the reset threshold: it determines an initial segment of the power-automaton distance profile and a sharp point at which the universal three-symbol-per-drop pattern ceases to be attainable.

## Limitations
The theorem concerns only the initial compression phase through deficiency \(h_n\) and proves only that the next target is strictly larger than the linear lower bound; it does not give a closed formula for \(\lambda_n(s)\) for all larger \(s\). The literature search cannot prove absolute novelty, and older subset-synchronization work could use terminology different from “rank compression.” The same-family primary sources and the targeted database/web searches inspected here did not reveal an equivalent statement.

## References
1. D. S. Ananichev, V. V. Gusev, M. V. Volkov, “Slowly synchronizing automata and digraphs,” arXiv:1005.0129v1, 2010.
2. D. S. Ananichev, V. V. Gusev, M. V. Volkov, “Primitive digraphs with large exponents and slowly synchronizing automata,” arXiv:1302.5793v2, 2013; J. Math. Sci. 192 (2013), 263–278.
