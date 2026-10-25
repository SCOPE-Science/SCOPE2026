# Isoperimetric sharp constants for sorting in convex weighted-path energies

## Finding
For an integer \(N\ge2\), let \(w_1,\ldots,w_{N-1}>0\). Let \(Sx\) be the increasing sorting of the real coordinates of \(x\in\mathbb R^N\). Let \(\Phi:[0,\infty)\to[0,\infty)\) be finite, nonzero, convex, nondecreasing, and satisfy \(\Phi(0)=0\). Define the convex edge energy
\[
\mathcal E_{w,\Phi}(x)=\sum_{i=1}^{N-1}w_i\Phi(|x_{i+1}-x_i|).
\]
For each \(1\le k\le N-1\), write \(P_N\) for the unit path on \(\{1,\ldots,N\}\) and set
\[
h_k(w)=\min_{\substack{A\subseteq\{1,\ldots,N\}\\|A|=k}}
\sum_{\substack{1\le i<N\\|A\cap\{i,i+1\}|=1}}w_i.
\]
Then the sharp one-input rearrangement energy multiplier is
\[
\boxed{\sup_{\mathcal E_{w,\Phi}(x)>0}
\frac{\mathcal E_{w,\Phi}(Sx)}{\mathcal E_{w,\Phi}(x)}
=\max_{1\le k<N}\frac{w_k}{h_k(w)}.}
\]
**This optimal multiplier is independent of the convex energy density \(\Phi\), including all power energies and finite Orlicz energies.** Every maximizing cut gives an actual attaining two-level vector, with an amplitude chosen so that \(\Phi\) is positive.

In particular, the following centered-defect families have complete, size-independent sharp phase diagrams. For \(N=2m\) with \(m\ge2\), put \(w_m=t>0\) and all other edge weights equal to one. Then
\[
\boxed{C_{2m}(t)=\max\{1,t/2\}.}
\]
For \(N=2m+1\) with \(m\ge2\), put \(w_m=w_{m+1}=t>0\) and all other edge weights equal to one. Then
\[
\boxed{C_{2m+1}(t)=\max\{1,t/2,1/(2t)\}.}
\]
Thus even centered defects are energy-contractive under increasing sorting for every \(0<t\le2\), whereas odd centered defects are contractive **exactly** for \(1/2\le t\le2\). As \(t\downarrow0\), the even multiplier stays one but the odd multiplier diverges like \(1/(2t)\).

## Assumptions and scope
All graphs here are finite *paths* with strictly positive edge weights; there are no vertex weights. Sorting is increasing and preserves multiplicities. The supremum is taken over real vectors with positive denominator. The function \(\Phi\) may have a zero interval but must be finite, convex, nondecreasing, nonnegative, vanish at zero, and not vanish identically. The multiplier compares the energy of **one rearranged vector** to its own energy; it is not a two-data Lipschitz modulus of the nonlinear map \(S\). The two centered families require at least four and five vertices respectively.

## Proof
**Step 1: convex superadditivity.** If \(a,b\ge0\) and \(a+b>0\), convexity and \(\Phi(0)=0\) give \(\Phi(a)\le a\Phi(a+b)/(a+b)\) and \(\Phi(b)\le b\Phi(a+b)/(a+b)\). Consequently \(\Phi(a+b)\ge\Phi(a)+\Phi(b)\). This extends inductively to every finite nonnegative sum.

**Step 2: ordered gaps and cuts.** Choose a rank ordering of the coordinates, resolving ties arbitrarily. Write their sorted values as \(y_1\le\cdots\le y_N\), and put \(g_k=y_{k+1}-y_k\ge0\). Let \(A_k\) be the set of original vertex positions carrying the \(k\) smallest ranked values. Along an original edge joining ranks \(a<b\), the absolute difference equals \(g_a+\cdots+g_{b-1}\). Step 1 implies
\[
\Phi(|x_{i+1}-x_i|)\ge
\sum_{k:\,|A_k\cap\{i,i+1\}|=1}\Phi(g_k).
\]
Multiplying by positive \(w_i\) and summing over original edges gives
\[
\mathcal E_{w,\Phi}(x)
\ge\sum_{k=1}^{N-1}\Phi(g_k)\,w(\partial A_k)
\ge\sum_{k=1}^{N-1}h_k(w)\Phi(g_k).
\]
By contrast, consecutive sorted values differ by exactly \(g_k\), so
\[
\mathcal E_{w,\Phi}(Sx)=\sum_{k=1}^{N-1}w_k\Phi(g_k)
\le\left(\max_k\frac{w_k}{h_k(w)}\right)\mathcal E_{w,\Phi}(x).
\]
Ties contribute \(\Phi(0)=0\), so no distinctness assumption is required.

**Step 3: sharpness and actual attainment.** Fix a cardinality \(k\) and choose an attaining cut \(A\) in the finite minimum defining \(h_k(w)\). Take \(x_i=0\) on \(A\) and \(x_i=a\) off \(A\), where \(a>0\) satisfies \(\Phi(a)>0\). Then \(\mathcal E_{w,\Phi}(x)=h_k(w)\Phi(a)\), and the sorted vector makes exactly one jump at edge \(k\), giving \(\mathcal E_{w,\Phi}(Sx)=w_k\Phi(a)\). Therefore every ratio \(w_k/h_k(w)\) is attained and the displayed multiplier is sharp.

**Step 4: a single central edge, even order.** Let \(N=2m\), \(m\ge2\), with central weight \(t\) and all others one. For any cardinality \(k\ne m\), every cut must cross a unit-weight edge; a prefix of size \(k\) has boundary weight one. Thus \(h_k(w)=1\). For cardinality \(m\), the two halves have boundary \(t\); any other cut must cross at least two unit edges or else both a unit and the central edge. A set consisting of the first \(m-1\) vertices and the last vertex achieves exactly two unit edges. Therefore \(h_m(w)=\min\{t,2\}\), proving the even formula.

**Step 5: two central edges, odd order.** Let \(N=2m+1\), \(m\ge2\), with the two edges incident to the middle vertex weighted \(t\), and every other edge weighted one. A cut not meeting a unit-weight edge must be formed from the three contiguous regions separated by the two central edges: the two outer regions of size \(m\) and the central singleton. The cuts of cardinality \(1\) or \(N-1\) have minimum weight \(\min\{1,2t\}\): either isolate an endpoint or isolate the central singleton. For cardinalities \(m\) and \(m+1\), the minimum is \(\min\{t,2\}\): the prefix/suffix cut has weight \(t\), and two separated endpoint blocks can be cut using two unit-weight edges. All remaining nontrivial cardinalities have minimum one because a unit edge must be crossed and a unit-edge prefix cut exists. Therefore \(w_k/h_k(w)\) has maximum \(\max\{1,t/2,1/(2t)\}\), proving the odd formula and all asserted sharp thresholds.

## Verification
A standalone checker, `CHECK.py`, uses only Python standard-library exact rational arithmetic. It enumerates all nonempty proper weighted cuts for representative arbitrary weights and centered defects, evaluates the claimed exact profiles for \(4\le N\le11\) and rational strengths on both sides of all thresholds, verifies energy inequalities for all ternary vectors through dimension six for five convex functions (including a convex function with a zero interval), and verifies explicit two-level equality witnesses. Running `python CHECK.py` produced:

`PASS: 140414 exact checks; central defect, cut profiles, convex energies, equality witnesses`

The infinite-family and all-convex-density statements follow from the written argument, not the finite checker. No symbolic software is required for the proof.

## Relationship to prior work
Bankevich–Nazarov (arXiv:1402.3006, first public 2014-02-12) investigate weighted continuous one-dimensional rearrangement inequalities and necessary/sufficient weight conditions. Gupta (arXiv:2204.11647, Theorem 2.2) proves a discrete weighted inequality for increasing half-line weights and power energies. Steinerberger (arXiv:2209.06765, Theorems 2 and 4) relates graph rearrangement to edge isoperimetry, supplying in particular a general \(\ell^1\) mechanism and a sufficient unweighted all-exponent condition. These antecedents motivate the comparison, but the inspected statements do not explicitly give the **sharp arbitrary-positive-weight finite-path multiplier simultaneously for every convex energy density**, nor the asymmetric low-strength defect instability distinguished by the odd/even centered formulas. The present argument is self-contained and uses the elementary level-set/cut ideas underlying this literature. The general \(\ell^1\) isoperimetric bound is acknowledged as an existing antecedent, not claimed independently.

## Limitations
The exact cut formula relies on the fact that sorted consecutive values lie on consecutive edges of a path. It is not stated for general graphs, multiple spatial dimensions, or nonconvex energy densities. It concerns one-input energy contraction, not two-input norm stability. The explicit defect formulas are only for the indicated symmetric weights; other weight patterns are covered by the finite cut formula but may have more complicated minimizing sets. The result has undergone self-review only; an independent audit has not been performed. Equivalent presentations in older weighted-rearrangement or edge-isoperimetric literature cannot be excluded.

## References
1. S. V. Bankevich and A. I. Nazarov, *On monotonicity of some functionals under rearrangements*, arXiv:1402.3006, first publicly available 2014-02-12. https://arxiv.org/abs/1402.3006
2. S. Gupta, *Symmetrization inequalities on one-dimensional integer lattice*, arXiv:2204.11647 (2022), especially Theorem 2.2. https://arxiv.org/abs/2204.11647
3. S. Steinerberger, *Discrete rearrangements and the Pólya–Szegő inequality on graphs*, arXiv:2209.06765 (2022), especially Theorems 2 and 4. https://arxiv.org/abs/2209.06765
