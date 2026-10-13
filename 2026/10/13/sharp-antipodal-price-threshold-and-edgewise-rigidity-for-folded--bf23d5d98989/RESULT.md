# Sharp antipodal-price threshold and edgewise rigidity for folded hypercube mixing

## Finding

**Theorem.** For any integer \(d\ge4\), set \(N=2^d\). Begin with the binary hypercube on \(\{0,1\}^d\) and add one antipodal edge between each vertex and its bitwise complement. Price every coordinate edge at one and each antipodal edge at \(t>0\). For **arbitrary independent nonnegative conductances** with priced sum one, the maximum spectral gap of the associated *unnormalized symmetric Laplacian* is
\[
\Gamma_d(t)=\begin{cases}
\dfrac{8}{N(d+t)},&0<t\le d,\\[4pt]
\dfrac{4}{dN},&t\ge d.
\end{cases}
\]
Here the two expressions agree at \(t=d\).

The following describes **every** maximizing edge allocation, not merely a symmetric representative. Let \(b\) denote the conductance of each coordinate edge and \(a\) that of each antipodal edge:

- If \(0<t<d\), the unique optimum has \(a=b=2/[N(d+t)]\): expensive and inexpensive edges receive the same conductance despite different prices.
- If \(t>d\), the unique optimum has \(a=0\) and \(b=2/(dN)\): every antipodal edge is deleted.
- If \(t=d\), precisely the symmetric one-parameter family \(a+b=2/(dN)\), \(0\le a\le b\), is optimal. No nonsymmetric optima occur, including at the transition.

For any fixed \(t>0\), the unique optimum eventually lies in the first regime as \(d\to\infty\). The total antipodal-edge expenditure fraction is \(t/(d+t)\to0\), yet its improvement over spending the entire budget on coordinate edges is
\[
\frac{\Gamma_d(t)}{4/(dN)}=\frac{2d}{d+t}\longrightarrow2.
\]
Thus a vanishingly small expenditure fraction on long-range antipodal links yields nearly twice the attainable spectral gap.

## Assumptions and scope

Vertices are bit strings \(x\in\{0,1\}^d\). For each coordinate \(i\in\{1,\ldots,d\}\), the undirected edge \(\{x,x\oplus e_i\}\) has conductance \(b_i(x)=b_i(x\oplus e_i)\ge0\). The antipodal edge \(\{x,\bar x\}\) has conductance \(a(x)=a(\bar x)\ge0\), where \(\bar x=x\oplus(1,\ldots,1)\). When \(d\ge4\), no antipodal edge coincides with a coordinate edge.

There are \(dN/2\) coordinate edges and \(N/2\) antipodal edges. The budget constraint is
\[
\sum_{e\ \mathrm{coordinate}} b_e+t\sum_{e\ \mathrm{antipodal}}a_e=1.
\]
The Laplacian \(L\) is the matrix whose quadratic form satisfies \(f^{\mathsf T}Lf=\sum_{\{x,y\}\in E}w_{xy}(f(x)-f(y))^2\). The objective is its second-smallest eigenvalue \(\lambda_2(L)\), equal to the spectral gap of the continuous-time symmetric generator \(-L\). This is **not** degree-normalized random-walk mixing or a worst-case total-variation mixing-time objective. Zero edge conductances are permitted; every optimal graph remains connected.

## Proof

Write \(B_i=\sum_{e\ \mathrm{coordinate\ in\ direction}\ i}b_e\), \(B=\sum_i B_i\), and \(A=\sum_{e\ \mathrm{antipodal}}a_e\). Define the mean edge-class weights \(b=2B/(dN)\), \(a=2A/N\). The budget becomes
\[
\frac N2(db+ta)=1.\tag{1}
\]
For each subset \(S\subseteq\{1,\ldots,d\}\), let \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\). For nonempty \(S\), this Walsh character is orthogonal to constants and has squared norm \(N\). Its Rayleigh quotient is precisely
\[
R(\chi_S)=\frac4N\left(\sum_{i\in S}B_i+ A\,\mathbf1_{|S|\ \mathrm{odd}}\right).
\]
Indeed each coordinate edge flips \(\chi_S\) exactly when its coordinate is in \(S\), and each antipodal edge flips it precisely when \(|S|\) is odd. Averaging the Rayleigh upper bounds for \(\lambda_2\) over all singleton characters, and separately over all two-coordinate characters, gives
\[
\lambda_2(L)\le \frac4N\left(\frac Bd+A\right)=2(b+a),
\qquad
\lambda_2(L)\le \frac{8B}{dN}=4b.
\tag{2}
\]
These bounds apply to every independently weighted allocation, without a symmetry assumption.

They are jointly sharp. When all coordinate edges have weight \(b\) and all antipodal edges have weight \(a\), each Walsh character is an exact Laplacian eigenvector with eigenvalue
\[
\Lambda_k=2kb+2a\,\mathbf1_{k\ \mathrm{odd}},\qquad 0\le k\le d.
\]
Because \(d\ge4\), the minimum over \(k\ge1\) is
\[
\lambda_2(L)=\min\{2(b+a),4b\}.\tag{3}
\]
Consequently (2) reduces the unrestricted graph problem *exactly* to maximizing (3) over \(a,b\ge0\) satisfying (1).

For \(a\ge b\), the objective is \(4b\), strictly decreasing as \(a\) increases under (1). For \(0\le a\le b\), the objective is \(2(b+a)\); substituting \(b=2/(dN)-(t/d)a\) gives an affine expression with slope \(2(1-t/d)\). Thus for \(t<d\) the maximum is uniquely at \(a=b=2/[N(d+t)]\); for \(t>d\) it is uniquely at \(a=0,b=2/(dN)\); and for \(t=d\) precisely the segment \(0\le a\le b\), \(a+b=2/(dN)\), attains the bound. Substitution yields the displayed value of \(\Gamma_d(t)\).

It remains to rule out hidden *nonsymmetric* optimizers. For an arbitrary optimal allocation, equality in the relevant averaged Rayleigh bound means each character in that average must itself have Rayleigh quotient \(\lambda_2\). By the variational characterization on the orthogonal complement of constants, it is then an **eigenvector** with eigenvalue \(\lambda_2\).

When \(t<d\), the unique optimal mean weights have \(a=b\), so both bounds in (2) are tight. Hence all singleton \(\chi_{\{i\}}\) and all pair \(\chi_{\{i,j\}}\) are eigenvectors for \(\lambda_2=:\gamma\). The eigenvector equation at each vertex for a pair character gives \(2[b_i(x)+b_j(x)]=\gamma\) for all distinct \(i,j\). With \(d\ge3\), these equations force \(b_i(x)=\gamma/4\) for every \(i,x\). The singleton eigenvector equations give \(2[b_i(x)+a(x)]=\gamma\), so \(a(x)=\gamma/4\) everywhere. This proves global uniqueness below threshold.

When \(t>d\), from (1) and the first bound (2) one obtains \(\lambda_2\le4/(dN)-4(t-d)A/(dN)\). Achieving \(4/(dN)\) therefore forces \(A=0\), hence every antipodal conductance vanishes. All singleton Rayleigh bounds then average to \(\lambda_2\), so every singleton is an eigenvector. Its pointwise eigenvector equation gives \(2b_i(x)=\gamma\) for each \(i,x\). Thus all coordinate conductances are equal, proving uniqueness above threshold.

Finally, when \(t=d\), the singleton average in (2) equals \(4/(dN)\) for **every feasible allocation**. At an optimum, all singletons are therefore eigenvectors. At each vertex their equations imply \(b_i(x)+a(x)=\gamma/2\) for every \(i\). Along a coordinate edge, the equality \(b_i(x)=b_i(x\oplus e_i)\) forces \(a(x)=a(x\oplus e_i)\). Because the coordinate hypercube is connected, \(a(x)\) is globally constant, and consequently all \(b_i(x)\) are globally constant. The Walsh eigenvalues above then show that \(\lambda_2=\gamma\) exactly when \(a\le b\). This proves that the displayed one-dimensional segment exhausts all optimizers.

## Verification

The accompanying standalone script `verify_folded.py` uses exact rational arithmetic and the Python standard library. It directly checks Walsh eigenvector equations on finite folded hypercubes, the global two-family Rayleigh bounds for independently irregular feasible allocations, and the entire displayed critical-segment construction at sample rational points. Execution yielded:

`VERIFY_OK 32256 exact Walsh component equations; 7500 exact character Rayleigh computations; 600 individually irregular feasible allocations; 12 critical-family spectra`

These finite computations are supplementary diagnostics. The preceding variational, Fourier and equality arguments prove the theorem for every integer \(d\ge4\) and every real \(t>0\). No finite test is presented as an exhaustive proof of arbitrary dimension.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis establish the general convex fastest-mixing *continuous-time* graph framework, but not a priced folded-hypercube formula or an arbitrary-edge optimizer classification. Boyd, Diaconis, Parrilo and Xiao analyze symmetry reductions and the *discrete-time ordinary hypercube*; their result neither varies antipodal-link prices nor proves the present all-edge rigidity. Shakeri and coauthors optimize algebraic connectivity when two given networks are joined by interlayer edges, holding intralayer networks fixed; this differs from simultaneously allocating the present coordinate and antipodal conductances.

Folded-hypercube Laplacian and resistance spectra have also been studied without price optimization, notably by Liu and coauthors and by Chen, Li and Lin. These spectral formulas motivate the Walsh decomposition, but do not state the threshold or characterize unrestricted price-optimal edge assignments. Combining symmetry averaging and known Fourier spectra suggests the two-class optimization; the additional equality argument establishes that **no unequal within-class assignment survives**. A directly equivalent historical specialization has not been conclusively excluded.

## Limitations

The theorem concerns symmetric continuous-time rates and the *combinatorial* spectral gap with a linear priced conductance budget, not normalized random walks or nonlinear physical energy prices. The bound \(d\ge4\) is part of the claim; low-dimensional graphical equivalences require separate treatment. Edge weights may be zero; imposing strictly positive weights would change the attained optimum above threshold. The proof does not establish optimal total-variation mixing times, stochastic-variance performance, or arbitrary directed-graph extensions. Scientific novelty is assessed against the cited and inspected literature, not certified against all unpublished or unindexed work. No independent scientific audit has been performed.

## References

1. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699; DOI: 10.1137/S0036144504443821. First published electronically November 2, 2006.
2. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819; DOI: 10.1137/070689413.
3. H. Shakeri and coauthors, *Maximizing Algebraic Connectivity in Interconnected Networks*, 2015 preprint, arXiv:1510.06785v1.
4. J.-B. Liu and coauthors, *The Kirchhoff Index of Folded Hypercubes and Some Variant Networks*, Mathematical Problems in Engineering (2014), article 380874; DOI: 10.1155/2014/380874.
5. H. Chen, X. Li, C.-K. Lin, *Random Walks on the Folded Hypercube*, Journal of Internet Technology 20 (2019), 1987–1994; https://jit.ndhu.edu.tw/article/download/2185/2198.
