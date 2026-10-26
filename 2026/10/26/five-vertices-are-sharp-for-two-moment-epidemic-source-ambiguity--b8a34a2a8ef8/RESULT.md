# Five vertices are sharp for two-moment epidemic-source ambiguity on paths

## Finding

**Theorem (sharp moment identifiability boundary).** Let \(P_n\) be the known, labeled path on \(n\ge2\) vertices. Independently retain each of its \(n-1\) edges with a common, *unknown* probability \(p\in(0,1)\). Let \(X_{n,k}(p)\) be the number of vertices in the retained-edge component of source \(k\). The observations are the exact population mean and variance of \(X\), not the identities of infected vertices.

1. For \(2\le n\le4\), equality of both moments under two source/parameter pairs forces the sources to lie in the same reflection orbit. Their transmission probabilities then agree.
2. **For every \(n\ge5\)**, there exist \(0<q<p<1\) such that distinct, non-reflection-equivalent sources \(2\) and \(3\) have identical mean and variance:
   \[
     \mathbb E X_{n,2}(p)=\mathbb E X_{n,3}(q),\qquad
     \operatorname{Var}(X_{n,2}(p))=\operatorname{Var}(X_{n,3}(q)).
   \]
3. Conversely, at any *known* \(p\in(0,1)\), the mean alone identifies the source up to reflection. The entire outbreak-size law also identifies both the unknown \(p\) and the source orbit: \(\Pr(X=n)=p^{n-1}\).

Thus the precise, nontrivial finite-path onset of **structural non-identifiability from two aggregate outbreak-size moments with unknown transmissibility** is five vertices, and it persists at every larger path order. The claim concerns only the independent-edge transmission model, not general correlated-duration SIR models.

For \(n=5\), the colliding source-2 parameter is the unique root in \((0,1)\) of
\[
 P(p)=p^9+5p^8+11p^7+7p^6-8p^5+56p^3+88p^2+32p-32,
\]
where \(411971/10^6<p<411973/10^6\), while the source-3 parameter \(q\) is the unique positive solution of \(2q+2q^2=2p+p^2+p^3\). Numerically \(p\approx0.4119719053\), \(q\approx0.3841902746\), and the common mean is approximately \(2.0635848835\). The exact all-size existence theorem does not require solving this polynomial.

## Assumptions and scope

The network \(P_n\) is labeled and fixed; the source is one vertex \(k\in\{1,\ldots,n\}\). Each potential transmission independently succeeds once with common probability \(p\); an epidemic reaches precisely the retained-edge connected component of its seed. An individual outbreak yields only its final **total** size. The two population moments could in principle be learned from arbitrarily many independent replicated outbreaks with unchanged source and parameters. Equality of source orbits means equality up to the sole nontrivial path automorphism \(k\mapsto n+1-k\). Only parameters strictly inside \((0,1)\) are claimed in the ambiguity result; at either boundary source identification has additional degeneracies. This finite, independent-bond construction must not be confused with SIR models having shared random infectious periods and correlated outgoing transmissions [1,2].

## Proof

**1. Exact moment laws.** For an arm of \(a\ge0\) edges emanating from the source, define \(Z_a\) to be the number of consecutive retained edges before the first failed edge or the end of the arm. It obeys \(\Pr(Z_a\ge j)=p^j\) for \(1\le j\le a\). Put
\[
 S_a(p)=\sum_{j=1}^a p^j,\qquad
 T_a(p)=\sum_{j=1}^a(2j-1)p^j,
 \qquad S_0=T_0=0.
\]
Tail sums give \(\mathbb E Z_a=S_a\) and \(\mathbb E Z_a^2=T_a\). For source \(k\), the left and right arms have lengths \(a=k-1\), \(b=n-k\), independently, so
\[
 \mu_{a,b}(p)=1+S_a(p)+S_b(p),\qquad
 V_{a,b}(p)=T_a(p)+T_b(p)-S_a(p)^2-S_b(p)^2.\tag{1}
\]
Every \(\mu_{a,b}\) increases strictly from \(1\) to \(n\) as \(p\) traverses \((0,1)\).

**2. Known transmission probability.** For adjacent sources,
\[
 \mu_{n,k+1}(p)-\mu_{n,k}(p)=p^k-p^{n-k}.
\]
It is strictly positive for \(k<n/2\). Hence a fixed \(p\) gives a strictly centerward-increasing mean on the reflection orbits. Moreover, to infect every vertex, every path edge must succeed, giving \(\Pr(X=n)=p^{n-1}\), so knowledge of the entire size law first determines \(p\) and then the source orbit.

**3. Orders below five.** Paths with at most two vertices have only one reflection orbit. For \(n=3\), compare endpoint source \((0,2)\) at probability \(p\) with center source \((1,1)\) at \(q\). Equality of means gives \(q=(p+p^2)/2\); substituting into (1) yields
\[
 V_{0,2}(p)-V_{1,1}(q)=\tfrac12p^2(1-p)(p+3)>0.
\]
For \(n=4\), compare endpoint \((0,3)\) at \(p\) with interior \((1,2)\) at \(q\). Equality of means reads
\[
 p+p^2+p^3=2q+q^2.\tag{2}
\]
At the same parameter \(p\), the interior mean exceeds the endpoint mean by \(p-p^3>0\), so (2) forces \(q<p\). Direct algebra from (1), using (2), gives
\[
 V_{0,3}(p)-V_{1,2}(q)=2p\big[p(1+2p)-q(1+p+p^2)\big]>0,
\]
since \(q<p\) and \(1+2p>1+p+p^2\) for \(0<p<1\). Therefore different source orbits cannot share both moments through order four; strict monotonicity of the mean in the parameter gives equality of probabilities within an orbit.

**4. Universal collision for every order \(n\ge5\).** Write \(m=n-2\ge3\). The two source arms are \((1,m)\) for vertex \(2\), and \((2,m-1)\) for vertex \(3\). For each \(p\in(0,1)\), let \(q(p)\in(0,1)\) be the unique solution of
\[
 \mu_{2,m-1}(q(p))=\mu_{1,m}(p).\tag{3}
\]
Since \(\mu_{2,m-1}(p)-\mu_{1,m}(p)=p^2-p^m>0\), we have \(q(p)<p\). Define the continuous equal-mean variance gap
\[
 \Delta_n(p)=V_{1,m}(p)-V_{2,m-1}(q(p)).\tag{4}
\]
For \(p\downarrow0\), equation (3) and (1) give
\[
 \mu_{1,m}(p)=1+2p+p^2+O(p^3),\quad
 \mu_{2,m-1}(q)=1+2q+2q^2+O(q^3),\quad
 q(p)=p-\tfrac12p^2+O(p^3).
\]
Also \(V_{1,m}(p)=2p+p^2+O(p^3)\) and \(V_{2,m-1}(q)=2q+4q^2+O(q^3)\). Consequently
\[
 \Delta_n(p)=-2p^2+O(p^3)<0\quad\text{for sufficiently small }p>0.\tag{5}
\]
To inspect the other boundary, for arms \((a,b)\) set
\[
 A_{a,b}=\sum_{j=1}^a j+\sum_{j=1}^b j,\qquad
 B_{a,b}=\sum_{j=1}^a j^2+\sum_{j=1}^b j^2.
\]
As \(r\uparrow1\), elementary expansion of (1) gives
\[
 n-\mu_{a,b}(r)=A_{a,b}(1-r)+O((1-r)^2),\quad
 V_{a,b}(r)=B_{a,b}(1-r)+O((1-r)^2).
\]
Thus, at a **common mean** \(n-\delta\), the variance is \(\delta B_{a,b}/A_{a,b}+O(\delta^2)\). Abbreviate \(A_1=A_{1,m}\), \(B_1=B_{1,m}\), \(A_2=A_{2,m-1}\), \(B_2=B_{2,m-1}\). Then
\[
 A_1-A_2=m-2,\qquad B_1-B_2=m^2-4,
\]
and hence
\[
 \frac{B_1}{A_1}-\frac{B_2}{A_2}
 =\frac{(m-2)((m+2)A_2-B_2)}{A_1A_2}>0.\tag{6}
\]
Indeed \(A_2=3+\sum_{j=1}^{m-1}j\), \(B_2=5+\sum_{j=1}^{m-1}j^2\), and every summand in \((m+2)A_2-B_2\) is positive because \(1\le j\le m-1<m+2\). Equation (6) makes \(\Delta_n(p)>0\) whenever \(p<1\) is sufficiently close to one. Combined with (5), continuity and the intermediate value theorem yield an interior solution \(\Delta_n(p)=0\). At that solution \(q(p)<p\), and the source orbits \(2\) and \(3\) are distinct for every \(n\ge5\). This proves the theorem.

**5. Exact smallest example.** For \(n=5\), equations (3)–(4) are two polynomials in \(p,q\). Eliminating \(q\) yields the resultant
\[
 4p^2(p-1)P(p).
\]
Here \(P(0)<0<P(1)\), and \(P'(p)>0\) on \((0,1)\): in the derivative, the only negative contribution \(-40p^4\) is dominated by \(168p^2\), with the remaining terms nonnegative and the constant strictly positive. Thus the unique interior resultant root is \(p\) above, and the existence proof already establishes that it corresponds to the admissible positive \(q\). Exact rational sign checks give the isolating interval printed in the Finding.

## Verification

Run \(\texttt{python verify.py}\) from the directory containing the two accompanying artifacts. The script requires Python 3 and SymPy 1.14; its standard output must equal \(\texttt{certificate.json}\) byte for byte (apart from no optional display formatting). It independently enumerates every retained-edge configuration on paths of orders \(2\) through \(9\) at three rational transmissibilities (132 source/parameter cases), recomputes means and variances from the resulting probability laws, checks the symbolic three- and four-vertex identities, derives the five-vertex resultant and rational isolating signs, and checks the near-one rational slope inequality over orders \(5\) through \(600\). Short-series expansions are also tested symbolically for orders \(5\) through \(13\). These finite tests **do not** establish the all-order statement; the analytical proof above does.

## Relationship to prior work

Karrer and Newman [2], inspected at the arXiv manuscript's sections II and IV, provide exact tree message-passing and bond-percolation generating functions, covering the forward computation of cluster-size distributions, but not the present inverse comparison under differing source positions and differing unknown edge probabilities. Kenah and Robins [1], inspected at the preprint introduction, model discussion, and component-distribution sections, distinguish independent bond percolation from correlated infectious-period SIR dynamics; they do not supply this finite-path inverse two-moment boundary. Shah and Zaman [3] examine infection-source recovery when the **set of infected vertices** is observed in an SI-type rumor-spread model; the data and dynamics differ from the present repeated **total-size-only** Reed–Frost/bond problem. Kiss and Simon [4], inspected in sections 2–5, investigate epidemic growth-rate/final-size identifiability in mean-field and network-derived compartment models, not exact source-orbit identification from finite-path outbreak-size moments. Existing exact mean-curve results for fixed sources on small trees address equality of the entire function in a common known parameter, rather than equality at *two different, unknown* transmission probabilities. These implications are distinct: equality of a full curve at the same parameter would be a much stronger constraint, whereas equality of two moments at differing parameters is possible here.

## Limitations

The collision does **not** show that the full outbreak-size distributions coincide, that source recovery is impossible with labeled infection observations, or that more than two outbreak moments cannot resolve ambiguity. It does **not** apply to general SIR dynamics where outgoing transmission events are correlated through random infectious periods. No unique crossover for arbitrary \(n\ge6\) is proved, and no robustness bound under finite-sample moment noise is claimed. The novelty assessment is literature-limited: unlocated equivalent results using truncated-geometric sums or percolation inverse-problem terminology remain possible; independent bibliographic assessment has not been undertaken.

## References

[1] E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, first public arXiv version 2006-10-30, arXiv:q-bio/0610057, later *Physical Review E* 76, 036113 (2007). https://arxiv.org/abs/q-bio/0610057 ; https://arxiv.org/pdf/q-bio/0610057

[2] B. Karrer and M. E. J. Newman, *A message passing approach for general epidemic models*, first public arXiv version 2010-03-29, arXiv:1003.5673, later *Physical Review E* 82, 016101 (2010). https://arxiv.org/abs/1003.5673 ; https://arxiv.org/pdf/1003.5673

[3] D. Shah and T. Zaman, *Rumors in a Network: Who's the Culprit?*, first public arXiv version 2009-09-24, arXiv:0909.4370; *IEEE Transactions on Information Theory* 57 (2011), 5163–5181. https://arxiv.org/abs/0909.4370

[4] I. Z. Kiss and P. L. Simon, *On Parameter Identifiability in Network-Based Epidemic Models*, *Bulletin of Mathematical Biology* 85, 18 (2023), DOI:10.1007/s11538-023-01121-y. https://link.springer.com/article/10.1007/s11538-023-01121-y
