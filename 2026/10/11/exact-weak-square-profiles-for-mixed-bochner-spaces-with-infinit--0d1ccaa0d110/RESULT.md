# Exact weak-square profiles for mixed Bochner spaces with infinite-dimensional atomic fibers

## Finding

Fix \(1<p<\infty\) and a finite positive measure space \((\Omega,\Sigma,\mu)\) whose nonatomic part has positive measure. Set \(Y=\ell_p(\mathbb N;\mathbb R)\) and \(X=L_1(\mu;Y)\). For \(x\in S_X\) let \(\Omega_{\mathrm{at}}\) be the measurable union of all positive-measure atoms, modulo null sets, and put
\[
a=\int_{\Omega_{\mathrm{at}}}\|x(\omega)\|_p\,d\mu(\omega),\qquad b=1-a.
\]
For every \(t\ge0\), define the pointwise sequential weak-square profile
\[
\Lambda_x(t)=\inf_{\substack{y_n\rightharpoonup0\\\|y_n\|_X\to t}}
\limsup_{n\to\infty}\max\{\|x+y_n\|_X,\|x-y_n\|_X\}.
\]
Then the following exact formula holds:
\[
\boxed{\Lambda_x(t)=\begin{cases}
1,&0\le t\le b,\\
b+\big(a^p+(t-b)^p\big)^{1/p},&t>b.
\end{cases}}
\]
Every infimum is achieved by a weakly null sequence whose norm is exactly \(t\) at each index. In particular, the norm-one defect is
\[
\Lambda_x(1)=b+2^{1/p}a=1+(2^{1/p}-1)a.
\]
Thus a unit vector is a weakly almost-square point precisely when it vanishes on the atomic component. The formula holds for arbitrarily many atoms and for every real exponent in the displayed interval.

## Assumptions and scope

All Banach spaces and weak topologies here are real. The measure is finite and positive; its nonatomic component has positive measure, while the number of atoms may be zero, finite, or countably infinite. Bochner functions are identified modulo almost-everywhere equality. On an atom a Bochner-integrable function is essentially constant. The value of an atomic coordinate is represented with its \(L_1\)-weighted norm, so that the atomic component is isometric to an \(\ell_1\)-sum of copies of \(Y\). No separability or countable generation of the measure algebra is needed. The infinite-dimensionality and \(p>1\) are essential to the atomic coordinate construction.

## Proof

**1. Decomposition and uniform atomic tails.** Write \(x=(u,f)\) in the isometric splitting
\[
X=\Big(\bigoplus_{j\in J}Y\Big)_{\ell_1}\oplus_1 L_1(\mu|_{\Omega\setminus\Omega_{\mathrm{at}}};Y).
\]
Here \(u=(u_j)\), \(a=\sum_j\|u_j\|_p\), and \(\|f\|_1=b\). Every element of the atomic sum has countable support. A weakly null sequence \(v_n\) in this sum has *uniformly small tails*: for every \(\varepsilon>0\) there is a finite \(F\subset J\) such that \(\sup_n\sum_{j\notin F}\|v_{n,j}\|_p<\varepsilon\). For completeness, otherwise inductively choose indices \(n_k\), pairwise disjoint successive finite coordinate blocks \(B_k\), and norm-one functionals \(\phi_k\) supported on \(B_k\), such that \(\phi_k(v_{n_k})>3\varepsilon/4\). Weak nullity permits the old-block functional \(\sum_{j<k}\phi_j\) to be smaller than \(\varepsilon/8\) on \(v_{n_k}\), and the right endpoint of \(B_k\) can be chosen to leave tail mass below \(\varepsilon/8\) for that fixed vector. The bounded functional \(\sum_k\phi_k\) then takes value above \(\varepsilon/2\) on every \(v_{n_k}\), a contradiction. For a noncountable index set, restrict to the countable union of supports of the sequence.

**2. The atomic lower bound.** For a bounded weakly null sequence \(v_n\) in the atomic sum, pass to a subsequence on which every coordinate norm \(\|v_{n,j}\|_p\) has a limit \(s_j\) and \(\|v_n\|\to s\). Step 1 implies \(s=\sum_j s_j\). Weak nullity implies coordinatewise convergence to zero in each \(\ell_p\). The elementary \(\ell_p\) splitting identity then yields for each \(j\) and both signs
\[
\|u_j\pm v_{n,j}\|_p^p-\|v_{n,j}\|_p^p\longrightarrow\|u_j\|_p^p.
\]
One proves this identity by truncating \(u_j\) to finitely many coordinates, using coordinatewise convergence there, and bounding the discarded tail by the mean-value estimate for the \(p\)-power of a norm; boundedness of \(v_{n,j}\) makes the error uniform. Uniform tails in Step 1 and summability of \(u\) now allow summation, so both signs have the same limit:
\[
\|u\pm v_n\|\longrightarrow \sum_j(\|u_j\|_p^p+s_j^p)^{1/p}
\ge (a^p+s^p)^{1/p}.
\]
The last inequality is Minkowski's inequality in the two-dimensional \(\ell_p\)-space, applied to the coordinate pairs.

**3. The diffuse lower bound and minimization.** Take any admissible weakly null \(y_n=(v_n,g_n)\) with \(\|y_n\|\to t\). Choose a subsequence realizing the limsup in the definition, then further subsequences for the atomic limits in Step 2 and the diffuse norm limit. Thus \(\|v_n\|\to s\in[0,t]\) and \(\|g_n\|\to t-s\). The triangle inequality gives
\[
\max\{\|f+g_n\|_1,\|f-g_n\|_1\}\ge \max\{b,\|g_n\|_1\}.
\]
Combining this with the common atomic limit from Step 2 gives
\[
\limsup_n\max\{\|x+y_n\|,\|x-y_n\|\}
\ge (a^p+s^p)^{1/p}+\max\{b,t-s\}.
\]
For \(s\in[0,t]\), the first summand is nondecreasing and has slope no larger than one; the second is \(t-s\) for \(s\le t-b\) and \(b\) for \(s\ge t-b\). Hence their sum is minimized at \(s=0\) when \(t\le b\), and at \(s=t-b\) when \(t>b\). This yields the stated lower bound, including the endpoints \(a=0\) and \(b=0\).

**4. Explicit simultaneous upper bounds.** On the nonatomic component choose a measurable sequence of signs \(r_n\in\{-1,1\}\) with \(hr_n\rightharpoonup0\) in \(L_1\) for every Bochner-integrable \(Y\)-valued function \(h\), and with \(\int h_0r_n\,d\mu\to0\) for every scalar \(h_0\in L_1\). Such Rademacher-type signs follow by successive equal-mass nonatomic partitions; the vector-valued weak-null conclusion follows first for simple functions and then by \(L_1\) approximation. Consequently, for \(c\ge0\),
\[
\|f\pm cfr_n\|_1\longrightarrow b\max\{1,c\}.
\]
If \(t\le b\) and \(b>0\), take \(y_n=(0,(t/b)fr_n)\); if \(t=b=0\), take the zero sequence. This gives the value \(1\).

Now suppose \(t>b\), and put \(s=t-b\). If \(a>0\), let \(e_n\) be the standard unit vector in \(Y\), set \(v_{n,j}=(s/a)\|u_j\|_p e_n\), and take \(y_n=(v_n,fr_n)\). Then \(\|y_n\|=s+b=t\). The sequence \(v_n\) is weakly null because \(e_n\rightharpoonup0\) in \(\ell_p\) and \(\sum_j\|u_j\|_p<\infty\). Moreover,
\[
\|u\pm v_n\|\longrightarrow (a^p+s^p)^{1/p},\qquad
\|f\pm fr_n\|_1\longrightarrow b.
\]
If \(a=0\), then \(b=1\) and the simpler sequence \(y_n=(0,tfr_n)\) has the same required limit \(t\), agreeing with the formula. The lower bound is attained in all cases. \(\square\)

## Verification

The proof uses only the explicit nonatomic sign construction, the gliding-hump uniform-tail lemma for weakly null sequences in an \(\ell_1\)-sum, coordinatewise \(\ell_p\) norm splitting, and finite-dimensional Minkowski. In the one-atom plus diffuse example with \(p=2\), \(a=3/10\), \(b=7/10\), and \(t=1\), the formula gives \(7/10+3\sqrt2/10\), whereas the scalar-fiber value is \(13/10\). This diagnostic separates the genuinely infinite-dimensional atomic mechanism from the scalar case; no finite computation is used as a proof.

## Relationship to prior work

Rodríguez and Rueda Zoca establish weak almost squareness of \(L_1(\mu;Y)\) when the entire measure is nonatomic, notably their Corollary 2.5 and the Rademacher-type sign argument. The present result recovers that case when \(a=0\), but determines an exact two-parameter profile when atoms are present, using the geometry of infinite-dimensional \(\ell_p\) fibers. Abrahamsen, Langemets, and Lima develop the original WASQ framework and qualitative sum-stability results; their statements do not supply the claimed pointwise profile. Quantitative static squareness parameters, without weakly null sequences, measure a different phenomenon.

## Limitations

The formula is proved only for real \(\ell_p\) fibers with \(1<p<\infty\) and a nonzero nonatomic measure component. It is not claimed for arbitrary Banach targets, \(p=1\), or \(p=\infty\). The theorem concerns weakly null sequences, not arbitrary weakly null nets. Published-literature comparison does not exclude equivalent results hidden in unindexed sources.

## References

1. J. Rodríguez and A. Rueda Zoca, *On weakly almost square Banach spaces*, arXiv:2301.07943v1 (first public version 2023-01-19), Section 2.2, Theorem 2.4 and Corollary 2.5. https://arxiv.org/html/2301.07943v1
2. T. A. Abrahamsen, J. Langemets, and V. Lima, *Almost square Banach spaces*, arXiv:1402.0818v2, Sections 1 and 5. https://arxiv.org/html/1402.0818v2
3. E. Oja, N. Saealle, and I. Zolk, *Quantitative versions of almost squareness and diameter 2 properties*, 2020, DOI:10.12697/ACUTM.2020.24.09 (distinction from quantitative static squareness parameters).
