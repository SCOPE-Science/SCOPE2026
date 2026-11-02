# A balance-dependent one-edge roundness reversal in complete bipartite metrics

## Finding

Let \(m,n\ge2\) be integers. Give one distinguished edge of the complete bipartite graph \(K_{m,n}\) length \(s\in[1,3]\) and every other edge length \(1\); let \(d_s\) be the induced shortest-path metric on all \(m+n\) vertices. Write \(\wp_{m,n}(s)\) for the supremal exponent of negative type of \((V,d_s)\). For \(p>0\), put
\[
 a=2^p,\qquad h=s^p-1,\qquad T=2mn-m-n,
\]
\[
 \mathcal F_{m,n}(p,s)=a^2\bigl(aT-2mn-2h\bigr)+h^2\bigl(2(m-1)(n-1)-a(2mn-3m-3n+4)\bigr).
\]
For \(m+n\ge5\), \(\wp_{m,n}(s)\) is the unique solution of \(\mathcal F_{m,n}(p,s)=0\) in \((0,1]\), and \(d_s\) has \(p\)-negative type exactly for \(0<p\le\wp_{m,n}(s)\). All smaller positive exponents have strict negative type. For \(m=n=2\), the unique critical exponent lies in \([1,2]\) and is determined by
\[
 (2^p-1)^2=s^p;
\]
its endpoints are \(\wp_{2,2}(1)=1\) and \(\wp_{2,2}(3)=2\).

The intact-biclique benchmark from Sánchez is
\[
 p_0=\wp_{m,n}(1)=\log_2\!\frac{2mn}{2mn-m-n}.
\]
Define
\[
 H_{m,n}=\frac{4m^2n^2}{(2mn-m-n)(m^2-m+n^2-n)}.
\]
For every \(s\in(1,3]\), there is the **exact sign trichotomy**
\[
 \wp_{m,n}(s)\begin{cases}>p_0,&s^{p_0}-1<H_{m,n},\\=p_0,&s^{p_0}-1=H_{m,n},\\<p_0,&s^{p_0}-1>H_{m,n}.
 \end{cases}
\]
Thus stretching a single edge always *improves* generalized roundness in balanced bicliques \(K_{k,k}\); yet in sufficiently unbalanced bicliques, stretching the edge far enough makes it *worse*. For example, on \(K_{2,8}\) the deletion-limit metric \(s=3\) satisfies \(\wp_{2,8}(3)<\wp_{2,8}(1)\), while all sufficiently small positive stretches improve the exponent.

For a fixed smaller part size \(m\), define \(p_\infty=\log_2(2m/(2m-1))\). Once the crossing lies below \(3\), its unique return length \(s_0(m,n)=(1+H_{m,n})^{1/p_0}\) obeys
\[
 \lim_{n\to\infty}n\bigl(s_0(m,n)-1\bigr)=\frac{4m^2}{(2m-1)p_\infty}.
\]
For every fixed \(s\in(1,3]\), the improvement of balanced bicliques has the sharp inverse-cubic scale
\[
 \lim_{k\to\infty}k^3\bigl(\wp_{k,k}(s)-\wp_{k,k}(1)\bigr)
 =\frac{\log s}{(\log 2)^2}.
\]
At a critical exponent, the snowflake metric \(d_s^{p/2}\) has minimum Euclidean embedding dimension \(m+n-2\), except that \((m,n,s,p)=(2,2,3,2)\) has dimension \(1\). Below the critical exponent its minimum dimension is \(m+n-1\).

## Assumptions and scope

All graph edges are undirected, lengths are positive, and all graph vertices are retained; no normalization to average masses is made. Here \(s=3\) is allowed because the distinguished endpoints are joined by a three-unit-edge alternate path. Distances between two vertices in the same part are \(2\), distances across distinct parts are \(1\), except for the distinguished pair, at distance \(s\). The term \(p\)-negative type means
\[
 \sum_{x,y}\alpha_x\alpha_y d_s(x,y)^p\le0
 \quad\text{for all real coefficients with }\sum_x\alpha_x=0.
\]
Strict negative type requires strict inequality for each nonzero such coefficient vector. The exponent \(p\) is not restricted to an integer. The \(s=3\) case is a shortest-path metric with one deleted edge, not a graph with a length-three direct shortcut.

## Proof

**1. Exact orthogonal quadratic-form reduction.** Let \(x\in\mathbb R^m\) and \(y\in\mathbb R^n\) be the two parts of a zero-sum coefficient vector. Put \(r=\sum_i x_i=-\sum_j y_j\); index the distinguished vertices by \(0\), and set \(u=x_0-r/m\) and \(v=y_0+r/n\). If \(\xi\) and \(\eta\) denote the respective zero-sum deviations of the *nondistinguished* coordinates around their means, then
\[
 -\alpha^\mathsf T D_p\alpha
 =a(\|\xi\|_2^2+\|\eta\|_2^2)
 +\begin{bmatrix}r&u&v\end{bmatrix}M\begin{bmatrix}r\\u\\v\end{bmatrix},
\]
where the symmetric matrix is
\[
 M=\begin{pmatrix}
 a(1/m+1/n)-2(a-1)+2h/(mn)&h/n&-h/m\\
 h/n&am/(m-1)&-h\\
 -h/m&-h&an/(n-1)
 \end{pmatrix}.
\]
Indeed the direct quadratic form is
\[
 \alpha^\mathsf TD_p\alpha=2(a-1)r^2-a(\|x\|_2^2+\|y\|_2^2)+2h x_0y_0,
\]
and the displayed block decomposition follows by expanding \(x_0=r/m+u\), \(y_0=-r/n+v\). The \(m+n-4\) fluctuation coordinates carry the strictly positive coefficient \(a\) in the negative quadratic form. Direct determinant expansion yields
\[
 \det M=-\frac{\mathcal F_{m,n}(p,s)}{(m-1)(n-1)}.
\]

**2. Exact scalar criterion for exponents at most one.** For \(0<p\le1\), concavity of the power function gives
\[
 0\le h\le3^p-1\le2(2^p-1)\le2^p=a.
\]
The bottom-right block of \(M\) has diagonal entries \(am/(m-1)>a\) and \(an/(n-1)>a\), with off-diagonal entry \(-h\). It is therefore positive definite. The Schur complement of this block is nonnegative exactly when \(\det M\ge0\), or \(\mathcal F\le0\). Hence this scalar inequality is necessary and sufficient for \(p\)-negative type for every \(p\in(0,1]\).

At \(p\downarrow0\), \(\mathcal F\to-(m+n)<0\). At \(p=1\), put \(h=s-1\in[0,2]\). By symmetry order the parts so that \(m\le n\). If \(m=2,n\ge3\), a direct simplification gives \(\mathcal F=2(h-2)^2+8(n-3)\); this vanishes only when \(n=3,s=3\). If \(m,n\ge3\), the quadratic coefficient of \(h\) in \(\mathcal F(1,s)\) is \(2[1-(m-2)(n-2)]\le0\), so the minimum over \([0,2]\) is at an endpoint. The two endpoint values are \(8[(m-1)(n-1)-1]>0\) and \(8(m+n-5)>0\). Thus \(\mathcal F(1,s)>0\) for all \(m+n\ge6\), and for \(m+n=5\) except the stated endpoint. By the general strict-negative-type inheritance theorem of Li and Weston, an interior zero of the determinant cannot precede a larger allowable exponent: any positive exponent strictly below the supremum has strict negative type. Continuity and the scalar criterion therefore give exactly one root in \((0,1]\). Moreover, the positive lower block makes its zero-sum equality space one-dimensional.

**3. Four vertices.** When \(m=n=2\), direct factorization gives
\[
 \mathcal F_{2,2}(p,s)=2(2a-h)\bigl((a-1)^2-s^p\bigr).
\]
For \(0<p<2\), \(h\le3^p-1<2^{p+1}=2a\), and the bottom block of \(M\) is positive definite. Thus the critical exponent solves \((2^p-1)^2=s^p\). The function \((2^p-1)^{2/p}\) is strictly increasing on \([1,2]\), from \(1\) to \(3\): differentiating its logarithm reduces positivity to \(z\log z>(z-1)\log(z-1)\) for \(z=2^p\ge2\). For \(s=3\), the four-point metric is a unit path of length three and has exact maximal negative type \(2\); its squared-distance centered Gram rank is one. At other critical parameters the lower block is positive and there is exactly one zero-sum equality direction.

**4. Sign of a one-edge stretch.** At the intact-biclique exponent \(p_0\), one has \(a_0=2mn/T\), so
\[
 \mathcal F_{m,n}(p_0,s)
 =h\left(-2a_0^2+\frac{2(m^2-m+n^2-n)}{T}h\right).
\]
Its sign is exactly that of \(h-H_{m,n}\). The scalar criterion, strictness below the maximal exponent, and the extension of strictness slightly beyond a strictly negative zero-sum form prove the trichotomy. When \(m=n=k\), \(H_{k,k}=k^2/(k-1)^2\), while
\[
 s^{p_0}-1\le3^{p_0}-1\le2(2^{p_0}-1)=\frac2{k-1}<H_{k,k},
\]
so every nontrivial stretch improves the exponent. For \((m,n)=(2,8)\), \(a_0=16/11\) and \(H=256/319\). The exact integer inequalities
\[
 16^{13}>2^7 11^{13},\qquad 3^7 319^{13}>575^{13}
\]
imply \(p_0>7/13\) and \(3^{p_0}-1>3^{7/13}-1>256/319\), hence the endpoint stretch decreases the exponent. Since \(H>0\), all sufficiently small stretches still improve it. The unique return length, when contained in \((1,3]\), follows by strictly increasing \(s\mapsto s^{p_0}-1\).

**5. Limits and embedding dimensions.** For fixed \(m\), the exact formula gives \(p_0\to p_\infty>0\) and \(nH_{m,n}\to4m^2/(2m-1)\). Expanding \((1+H)^{1/p_0}\) proves the return-length limit. For balanced parts \(k=k\), the positive Schur complement in step 2 has value \(2h/k^2+O(h^2/k^2)\) at \(p_0\); uniformly for fixed \(s\), \(h=s^{p_0}-1=(\log s)/(k\log2)+O(k^{-2})\), while the derivative of the Schur complement with respect to \(p\) is \(-2\log2+O(k^{-1})\). The implicit root shift is therefore \((\log s)/(k^3(\log2)^2)+o(k^{-3})\). Finally, Schoenberg's centered Gram criterion gives the Euclidean rank as the dimension of the strictly positive part of \(-\tfrac12 JD_pJ\). The decomposition in step 1 yields rank \(m+n-1\) below the endpoint and \(m+n-2\) at it, except for the path exception discussed in step 3.

## Verification

The self-contained Python program `verify_one_edge_biclique.py` checks the quadratic-form identity and determinant by exact rational arithmetic, compares the critical equations against full centered distance-matrix spectra, supplies exact integer inequalities for the \(K_{2,8}\) reversal, and checks the balanced and unbalanced asymptotic scales at increasing sizes. Install dependencies from `requirements.txt`, then run `python verify_one_edge_biclique.py`. The finite tests corroborate, but do not substitute for, the proof above.

## Relationship to prior work

Li and Weston prove the strictness and interval inheritance principle for finite negative-type metrics. Sánchez determines the supremal negative type of the *unperturbed* complete bipartite graph and gives a general distance-matrix method; the intact benchmark above is that earlier result. Robertson derives Hilbert distortion and negative-type formulas for the uniform complete bipartite metric, again not for a singled-out edge. Sun and Wan, building on Varghese–So–Vijayakumar, analyze how deleting an edge changes the **distance energy** of a biclique, not the conditional negative-type inequalities, and obtain an always-increasing distance-energy result. The present theorem compares every intermediate edge length, proves an exact opposite-direction phenomenon for the roundness exponent, and quantifies two distinct asymptotic sensitivities. General determinant formulas do not supply these family-specific sign and asymptotic conclusions without the reduction and analysis given here.

## Limitations

The theorem concerns a single lengthened bipartite edge, with all remaining edges of length one, and \(2\le m,n<\infty\). It does not classify simultaneous multiple-edge perturbations, arbitrary conductances, or graph metrics outside this family. The critical Euclidean dimension pertains to the snowflaked distance \(d_s^{p/2}\), not to a claim that the original distance is always Euclidean. An unindexed equivalent formulation remains a possible literature risk. The asymptotic constants are for the stated fixed-parameter regimes; no uniform two-parameter asymptotic is claimed.

## References

1. H. Li and A. Weston, *Strict p-negative type of a metric space*, first publicly posted 6 January 2009, arXiv:0901.0695, https://arxiv.org/abs/0901.0695.
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, first publicly posted 2 August 2011, arXiv:1108.0451, https://arxiv.org/abs/1108.0451.
3. G. Robertson, *Negative type and bi-lipschitz embeddings into Hilbert space*, first publicly posted 27 September 2023, arXiv:2309.16070, https://arxiv.org/abs/2309.16070.
4. S. Sun and Z. Wan, *On the Change of Distance Energy of Complete Bipartite Graph due to Edge Deletion*, first published 9 January 2021, DOI:10.1155/2021/6678248, https://doi.org/10.1155/2021/6678248.
