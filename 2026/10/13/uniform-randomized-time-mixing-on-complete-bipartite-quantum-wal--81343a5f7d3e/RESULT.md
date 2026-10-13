# Uniform randomized-time mixing on complete bipartite quantum walks

## Finding

**Theorem.** Let \(m,n\geq1\) be integers, let \(G=K_{m,n}\) be the simple unweighted complete bipartite graph, and let \(A\) be its adjacency matrix. For each real \(t\), put \(U(t)=\exp(\mathrm{i}tA)\) and define the entire quantum-walk mixing matrix \(M(t)_{uv}=|U(t)_{uv}|^2\). A single Borel probability measure \(\mu\) on observation times is used for **every** initial vertex. Then

\[
\int_{\mathbb R}M(t)\,\mathrm d\mu(t)=\frac{1}{m+n}J_{m+n}
\quad\Longleftrightarrow\quad
\{m,n\}\in\big\{\{1,1\},\{1,2\},\{1,3\},\{2,2\}\big\}.
\]

The necessity covers *all* probability measures, not merely finite-support, Gaussian, or absolutely continuous sampling laws. All four admissible graph types have explicit sampling measures. Thus randomized observation times create uniform average mixing on the three-vertex path, but cannot enable it on any other complete bipartite graph beyond the three types already allowing instantaneous full-matrix uniform mixing.

For the first excluded star \(K_{1,4}\), there is also a quantitative obstruction: for every such \(\mu\),
\[
\max_{u,v}\left|\int M(t)_{uv}\,\mathrm d\mu(t)-\frac15\right|\geq\frac{2}{45}.
\]
This lower bound is not asserted to be optimal.

## Assumptions and scope

The graph has \(m+n\) labeled vertices, divided into nonempty parts of respective cardinalities \(m\) and \(n\). Every cross-part pair is joined by one edge of hopping strength one, and there are no within-part edges, loops, onsite terms, control pulses, or time-dependent couplings. The Hamiltonian is the **ordinary adjacency matrix**, not a normalized or combinatorial Laplacian. The sign of the exponent is immaterial for squared entry moduli. The probability measure is chosen once and must make all \((m+n)^2\) entries equal simultaneously. Integrals exist because every entry lies in \([0,1]\).

Write \(N=m+n\), \(\omega=\sqrt{mn}\), and \(X=\cos(\omega T)\) for a real random observation time \(T\sim\mu\). Then \(-1\leq X\leq1\) almost surely. Conversely, any finitely supported probability law on \([-1,1]\) is implementable by selecting times \(T=\arccos(X)/\omega\).

## Proof

Ordering the vertices by bipartition, the adjacency matrix satisfies
\[
A=\begin{pmatrix}0&J_{m,n}\\J_{n,m}&0\end{pmatrix},
\qquad A^2=\begin{pmatrix}nJ_m&0\\0&mJ_n\end{pmatrix},
\qquad A^3=mnA.
\]
Expanding the exponential using the last identity gives, without any spectral simplicity hypothesis,
\[
U(t)=I+\frac{\cos(\omega t)-1}{mn}A^2
+\frac{\mathrm{i}\sin(\omega t)}{\omega}A.
\]
Consequently, at a time with \(x=\cos(\omega t)\), the four entry types of \(M(t)\) are as follows. Distinct vertices in the \(m\)-part have squared amplitude \((1-x)^2/m^2\); diagonal vertices in that part have \((1+(x-1)/m)^2\). Replace \(m\) by \(n\) for the other part. Any cross-part entry is
\[
M(t)_{uv}=\frac{1-x^2}{mn}\quad(u\text{ and }v\text{ in different parts}).
\]

If \(m,n\geq2\), a uniform expected cross-part entry would require \(\mathbb E(1-X^2)=mn/N\). The left side is at most one. Therefore \(mn\leq m+n\), or \((m-1)(n-1)\leq1\). Both factors are positive integers, so \(m=n=2\) is the only possibility. When \(m=n=2\), take \(t=\pi/4\), for which \(\cos(\omega t)=0\); every one of the sixteen squared entries then equals \(1/4\).

Now suppose \(m=1\) and \(n\geq2\). The hub's diagonal entry is \(X^2\), and the entry between two distinct leaves is \((1-X)^2/n^2\). Their required common mean \(1/(n+1)\) forces
\[
\nu:=\mathbb E(X^2)=\frac1{n+1},\qquad
\frac{1-2\eta+\nu}{n^2}=\frac1{n+1},\qquad
\eta:=\mathbb E X=-\frac{n-2}{2}.
\]
For \(n\geq5\), this contradicts \(\eta\geq-1\). For \(n=4\), it forces \(X=-1\) almost surely, which implies \(\nu=1\), contradicting \(\nu=1/5\). Therefore \(n\leq3\). Exchanging the two parts handles \(n=1\).

All remaining possibilities are attained as follows, with \(T\) in the same hopping-time units as \(U(t)\):

- \(K_{1,1}\): choose the deterministic time \(T=\pi/4\).
- \(K_{1,2}\): give the three times \(0,\ \pi/(2\sqrt2),\ \pi/\sqrt2\) respective probabilities \(1/6,\ 2/3,\ 1/6\). Then \(\eta=0\), \(\nu=1/3\), and all nine expected squared amplitudes equal \(1/3\).
- \(K_{1,3}\): choose deterministic \(T=2\pi/(3\sqrt3)\), for which \(X=-1/2\); every squared amplitude is \(1/4\).
- \(K_{2,2}\): the deterministic time above gives every squared amplitude \(1/4\).

For the quantitative \(K_{1,4}\) assertion, put \(\delta=\max_{u,v}|\mathbb E M(T)_{uv}-1/5|\), \(\eta=\mathbb EX\), and \(\nu=\mathbb E X^2\). The hub-diagonal and distinct-leaf entries imply
\[
\nu\leq\frac15+\delta,
\qquad\frac{1-2\eta+\nu}{16}\geq\frac15-\delta,
\qquad\eta\leq-1+\frac{17}{2}\delta.
\]
But \(\mathbb E(1+X)^2\geq0\) gives \(\nu\geq-1-2\eta\geq1-17\delta\). Thus \(1-17\delta\leq1/5+\delta\) and \(\delta\geq2/45\), as asserted.

## Verification

The accompanying standard-library-only script `verify.py` checks the exact matrix identity \(A^3=mnA\) and squared-entry stochasticity for all \(225\) ordered pairs \(1\leq m,n\leq15\) at seven rational cosine values; verifies exact uniform averages for the three cases with rational cosine moments; checks the separate single-edge identity; and evaluates \(1445\) two-point rational observation laws for the quantitative four-leaf obstruction. It returns a `VERIFY_OK` message with the counts. Every statement for unbounded \(m,n\) is established by the displayed algebraic proof, not by finite enumeration.

Replay: extract `verify.py` from this package into a writable directory, then run `python3 verify.py`. The script needs only Python 3 and its standard library.

## Relationship to prior work

Baptista, Coutinho, and Marques introduce averages of mixing matrices under arbitrary sampling distributions and in Proposition 9 rule out \(K_{m,n}\) with \(m+n>7\) by a trace bound; they identify the four positive bicliques above but leave further low-order bicliques unresolved [1, Section 3.1]. The present theorem supplies the missing **necessity** for every remaining size, by using individual cross-part and leaf-pair matrix entries rather than only the spectrum's multiplicities. Positive examples are credited to that work and its references; their existence is not asserted to be newly discovered here.

Carlson, Ford, Harris, Rosen, Tamon, and Wrobel study instantaneous mixing with adjustable edge weights and/or a fixed initial vertex [2, Sections 2–4]. Their weighted universal-mixing constructions do not imply uniformity of the full mixing matrix for one fixed **unweighted** graph and one common random-time law. The journal version of [1] was also checked at its publisher's bibliographic/abstract level [3]; its full text was not available there. The matching preprint [1] was read directly.

## Limitations

This classification does not address unequal edge weights, onsite potentials, normalized-Laplacian walks, different sampling laws for different initial vertices, approximate mixing outside the displayed lower bounds, or other graph families. The four possible bicliques and their positive mixing behavior were already identified in [1]; the new mathematical content is a complete all-orders exclusion of other bicliques and the explicit nonzero obstruction for \(K_{1,4}\). Equivalent less-visible characterizations in subsequent literature remain a residual originality risk.

## References

[1] P. Baptista, G. Coutinho and V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (first public 2023-08-31), Section 2 and Proposition 9 in Section 3.1. Full preprint: https://arxiv.org/html/2308.16378v1 . Published as *Quantum Information Processing* **23**, article 272 (2024), DOI:10.1007/s11128-024-04480-0.

[2] W. Carlson, A. Ford, E. Harris, J. Rosen, C. Tamon and K. Wrobel, *Universal Mixing of Quantum Walk on Graphs*, arXiv:quant-ph/0608044v1 (2006). Full preprint: https://arxiv.org/html/quant-ph/0608044v1 .

[3] Springer Nature, publisher's bibliographic record and abstract for DOI:10.1007/s11128-024-04480-0: https://link.springer.com/article/10.1007/s11128-024-04480-0 .
