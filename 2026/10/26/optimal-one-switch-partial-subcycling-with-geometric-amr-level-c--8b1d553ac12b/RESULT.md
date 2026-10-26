# Optimal one-switch partial subcycling with geometric AMR level costs

## Finding

In a geometric adaptive-mesh-refinement (AMR) hierarchy with a nonnegative fine-side coordination charge per active temporal interface, **every globally minimum-cost binary subcycling schedule locks an initial group of coarse levels and subcycles all remaining finer levels**. There is an explicit finite-depth threshold rule and a sharp geometric-growth phase boundary.

Precisely, fix integers \(r\ge 2\) and \(L\ge 1\), a cell-cost scale \(c>0\), a geometric growth factor \(\rho\ge 1\), and an overhead coefficient \(h\ge 0\). Set \(w_\ell=c\rho^\ell\), \(0\le\ell\le L\). On each adjacent boundary \(i=1,\ldots,L\), a binary decision \(b_i=1\) makes level \(i\) execute \(r\) steps per step of level \(i-1\); \(b_i=0\) locks their steps. Fix the finest-level step count \(\nu_L=r^L\) over the common physical window and determine other counts from \(\nu_{i-1}=\nu_i/r^{b_i}\). The exact modeled work is
\[
  C(b)=\sum_{\ell=0}^L\nu_\ell w_\ell
       +h\sum_{i=1}^L b_i\nu_i w_i.
\]
The second term is a **specified** extra coordination cost, proportional to the fine-side updates at an active boundary; it is not asserted to be an empirical identity for arbitrary AMR codes.

Define strictly increasing finite-level thresholds
\[
  \theta_j=\left(1-\frac1r\right)\sum_{t=1}^{j}\rho^{-t},\qquad 1\le j\le L.
\]
Every minimizer is a suffix schedule \(b_i=0\) for \(i\le k\), \(b_i=1\) for \(i>k\), with \(0\le k\le L\), and its cost is
\[
 C_k=r^k\sum_{\ell=0}^{k}w_\ell+(1+h)\sum_{\ell=k+1}^{L}r^\ell w_\ell.
\]
The minimizing \(k\) is the first \(k\in\{0,\ldots,L-1\}\) with \(h\le\theta_{k+1}\), or \(k=L\) if none exists. For \(h=\theta_j\), and only then, exactly two schedules tie: \(k=j-1\) and \(k=j\). At all other \(h\), the minimizer is unique.

For \(\rho>1\), put \(h_c=(1-1/r)/(\rho-1)\). Every finite hierarchy has **uniquely optimal global stepping** (all \(b_i=0\)) for \(h\ge h_c\). For each fixed \(0\le h<h_c\), the optimizing locked-prefix depth is bounded independently of \(L\) as \(L\to\infty\). By contrast, for \(\rho=1\), every finite \(h\) still favors some subcycling for all sufficiently deep hierarchies, and the optimizing prefix depth remains bounded as \(L\) grows. When \(\rho=r^\delta\), the existence of a finite hierarchy-independent global-stepping threshold is therefore equivalent to positive feature dimension \(\delta>0\) within this model.

## Assumptions and scope

The hierarchy advances \(L+1\) levels with exactly geometric positive work weights. Each temporal refinement edge allows precisely a multiplier \(1\) or \(r\); the finest level is held at \(r^L\) updates per common physical window. Uniform work per updated cell is absorbed into \(c\), and independent active-interface overhead is charged as \(h\nu_i w_i\). No restriction is imposed on the binary pattern before optimization: all \(2^L\) choices are eligible. The normalization to a fixed finest-level count is essential when comparing schedules. The theorem concerns this deterministic work count, not observed wall-clock time, solver accuracy, stability, or a code with different per-interface charges.

## Proof

**1. Exact change on exchanging an inverted pair.** Consider any consecutive decisions \((b_i,b_{i+1})=(1,0)\), where \(1\le i<L\). Write \(T=\nu_{i+1}\). Before the swap, \(\nu_i=T\), \(\nu_{i-1}=T/r\); after exchanging the decisions to \((0,1)\), \(\nu_i=T/r\), \(\nu_{i-1}=T/r\). No other level's update count changes. The update-work change is \(-(1-1/r)Tw_i\). The overhead changes from \(hTw_i\) to \(hTw_{i+1}\). As \(w_{i+1}=\rho w_i\), the exact total difference is
\[
 C(\ldots,0,1,\ldots)-C(\ldots,1,0,\ldots)
   =Tw_i\left[h(\rho-1)-\left(1-\frac1r\right)\right].
\]
When \(\rho=1\), this is strictly negative for all finite \(h\). When \(\rho>1\) and \(h<h_c\), it is also strictly negative. Repeatedly exchanging inverted pairs reduces the cost until the ones form a suffix. Hence in either regime **no nonsuffix pattern can minimize**.

**2. Large-overhead global optimum, including equality.** For an arbitrary binary pattern, the update counts satisfy
\[
 \nu_i-\nu_{i-1}=\left(1-\frac1r\right)b_i\nu_i.
\]
Telescoping gives \(r^L-\nu_\ell=(1-1/r)\sum_{i=\ell+1}^Lb_i\nu_i\). Comparing the arbitrary schedule to global stepping yields the exact identity
\[
 C(b)-C_{\mathrm{global}}=
 \sum_{i=1}^{L} b_i\nu_i w_i
 \left[h-\left(1-\frac1r\right)
 \frac{\sum_{\ell=0}^{i-1} w_\ell}{w_i}\right]
 =\sum_{i=1}^{L} b_i\nu_iw_i(h-\theta_i).
\]
If \(\rho>1\), every finite \(\theta_i<h_c\); thus \(h\ge h_c\) makes every nonzero summand strictly positive. The all-locked schedule is uniquely optimal, even at \(h=h_c\).

**3. Optimize the suffix schedules.** For an integer \(k\in[0,L]\), a suffix schedule has \(\nu_\ell=r^k\) on \(\ell\le k\) and \(\nu_\ell=r^\ell\) on \(\ell>k\), giving the claimed formula for \(C_k\). Adjacent costs obey
\[
 C_{k+1}-C_k=(r-1)r^k\sum_{\ell=0}^{k}w_\ell
                   -hr^{k+1}w_{k+1}
                 =r^{k+1}w_{k+1}(\theta_{k+1}-h).
\]
Since \(\theta_1<\cdots<\theta_L\), the cost sequence decreases before the first \(\theta_{k+1}\ge h\) and increases after it; a single equality yields exactly two adjacent ties. In the remaining regime \(h\ge h_c\), Part 2 already gives \(k=L\) uniquely, matching the threshold rule.

**4. Depth and dimension transition.** If \(\rho>1\), \(\theta_j\) increases to \(h_c\) from below; every \(h<h_c\) crosses a finite \(\theta_j\) (or \(h=0\) selects \(k=0\)), so the minimizing locked-prefix length becomes independent of \(L\) once \(L\) exceeds the crossing depth. If \(\rho=1\), \(\theta_j=j(1-1/r)\) increases without bound, and every fixed finite overhead is crossed at a finite \(j\). Thus global stepping ceases to minimize once the depth exceeds that index. All statements follow.

## Verification

The attached standalone `verify.py` computes every one of \(2^L\) patterns exactly using rational arithmetic, then compares the set of minimizers against the threshold-selected suffix schedules for \(1\le L\le8\), \(r\in\{2,3,4\}\), \(\rho\in\{1,2,3,5/2\}\), and representative and equality-threshold overhead values. Its recorded output states `EXACT_RATIONAL_ENUMERATION_PASS 1790`. These finite checks are a reproducibility aid, not a substitute for the all-depth proof above.

For a concrete partial optimum, let \(r=2\), \(\rho=2\), \(L=4\), \(c=1\), and \(h=1/3\). Then \(\theta_1=1/4<h<\theta_2=3/8\), so the unique optimum locks boundary 1 and subcycles boundaries 2, 3, and 4; it has work \(C_1=454\), compared to \(C_0=1363/3\) for full subcycling and \(C_4=496\) for global stepping.

## Relationship to prior work

Hyman's 2026 analysis states the multilevel work identity for any **prescribed** subcycling schedule and obtains closed cell-count speedups for geometric hierarchies and global-versus-full-subcycling comparisons. It explicitly singles out minimizing work plus schedule-dependent overhead as a remaining question. The present theorem supplies the exact optimizer among **all binary partial-subcycling patterns** under the new, explicitly fixed overhead function \(h\sum_i b_i\nu_iw_i\). The parameter \(h\) is not Hyman's normalized aggregate overhead, so the numerical break-even thresholds are not interchangeable.

Almgren and colleagues' 2013 Nyx paper documents automatic and manually selectable partial subcycling, including heterogeneous patterns, but not this geometric weighted-work cutoff and its proof. The Nyx automatic scheduler is a broader application-oriented selection mechanism, not a source for claiming a general scheduling optimum here. The theorem does not supersede arbitrary scheduling or measured-overhead optimization.

## Limitations

No claim is made for real runtimes, irregular or only approximately geometric cell counts, variable per-level kernel costs, negative overheads, nonadditive synchronization/communication, step ratios other than \(1\) and \(r\), adaptive accuracy constraints, floating-point errors, or hardware parallelism. The simple fine-side-charge model can differ from actual AMR implementations. Earlier work on optimal-subcycling enumeration or unpublished implementation details may contain an equivalent characterization under another cost model; the analytic novelty is bounded to the stated exact cost functional and the classification above.

## References

1. J. M. Hyman, *When Is Local Time Stepping Worthwhile? A Cost Analysis for Nested Adaptive Mesh Refinement*, arXiv:2610.15143v1, 10 October 2026. https://arxiv.org/html/2610.15143v1
2. A. S. Almgren, J. B. Bell, M. J. Lijewski, Z. Lukić, and E. Van Andel, *Nyx: A Massively Parallel AMR Code for Computational Cosmology*, *Astrophysical Journal* **765** (2013), 39, Section 4.2. https://doi.org/10.1088/0004-637X/765/1/39
3. Nyx documentation, *Inputs: Subcycling*, describing manually selected adjacent ratios. https://amrex-astro.github.io/Nyx/docs_html/NyxInputs.html
