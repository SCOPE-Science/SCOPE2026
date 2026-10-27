# A sharp support-gap law for cyclic flat dilation in bounded variation

## Finding

Fix any integer \(n\ge3\), and let \(V_n(z)=\sum_{i=0}^{n-1}|z_{i+1}-z_i|\) for real cyclic vectors, with indices modulo \(n\). For the flat dilation by a consecutive window \(I_\ell=\{0,1,\ldots,\ell-1\}\), \(1\le\ell\le n\), let
\[
 (D_\ell x)_i=\max_{0\le j<\ell}x_{i+j}.
\]
Its sharp two-input bounded-variation Lipschitz multiplier is
\[
\sup_{V_n(x-y)>0}\frac{V_n(D_\ell x-D_\ell y)}{V_n(x-y)}=
\begin{cases}1,&1\le\ell<n,\\0,&\ell=n.\end{cases}
\]
For the minimally gapped two-tap window \(B=\{0,2\}\), let \((G_nx)_i=\max\{x_i,x_{i+2}\}\). Then the sharp two-input multiplier is
\[
\boxed{\sup_{V_n(x-y)>0}\frac{V_n(G_nx-G_ny)}{V_n(x-y)}=
\begin{cases}1,&n=3,\\2,&n=4,5,\\3,&n\ge6.\end{cases}}
\]
In contrast, the sharp *one-input* factor for the gapped window is \(1\) for \(n=3\) and \(2\) for every \(n\ge4\). Every supremum in these statements is attained by explicit finite real inputs.

## Assumptions and scope

All signals are real, indexed by the cyclic group \(\mathbb Z/n\mathbb Z\), and both operators are applied once. The same seminorm \(V_n\) measures input and output differences. The operators preserve additive constants, so pairs with \(V_n(x-y)=0\) cause zero output variation and can be ignored when forming the quotient. The windows are unweighted, flat, and translation-invariant. All integer and real parameter quantifiers are as displayed.

## Proof

**1. A general selector reduction.** Fix two inputs \(x,y\), put \(h=x-y\), and follow the segment \(z(t)=y+th\), \(0\le t\le1\). Each coordinate of any finite flat dilation \(F(z(t))\) is a maximum of finitely many affine functions of \(t\), hence is absolutely continuous and piecewise affine. Away from finitely many relevant crossings it has derivative \(h_{\sigma_t(i)}\), for a maximizing window index \(\sigma_t(i)\). In a permanent tie the tied affine functions have identical slope, so the derivative remains well-defined almost everywhere. The fundamental theorem of calculus and convexity of \(V_n\) imply
\[
V_n(F(x)-F(y))\le\int_0^1 V_n\bigl((h_{\sigma_t(i)})_{i=0}^{n-1}\bigr)\,dt.
\]
It suffices to bound every corresponding selector in the \(V_n\)-seminorm.

**2. Consecutive windows are nonexpansive.** For a cyclic signal lifted periodically to integer indices and an interval of length \(\ell<n\), choose \(\sigma(i)\) as the rightmost maximizing index in \([i,i+\ell-1]\). Then \(\sigma(i+1)\ge\sigma(i)\): either the old maximizer survives the one-step slide, or the discarded left endpoint is replaced by a later index. Moreover \(\sigma(i+n)=\sigma(i)+n\). Thus the consecutive integer arcs from \(\sigma(i)\) to \(\sigma(i+1)\) partition one complete period of input edges, possibly with empty arcs. The triangle inequality gives
\[
 \sum_{i=0}^{n-1}|h_{\sigma(i+1)}-h_{\sigma(i)}|
 \le\sum_{k=\sigma(0)}^{\sigma(0)+n-1}|h_{k+1}-h_k|=V_n(h).
\]
The selector reduction proves two-input nonexpansivity. For \(\ell=n\), each output is the global maximum, hence is a constant cyclic vector, so its variation is zero. For every \(\ell<n\), take \(x=(1+\varepsilon)e_0\), \(y=e_0\), \(\varepsilon>0\), where \(e_0\) is a single-site indicator. Their dilation difference is \(\varepsilon\) times the indicator of \(\ell\) successive sites and has exactly the same variation \(2\varepsilon\) as \(x-y\). This proves sharpness.

**3. The gapped two-tap universal bound.** For each selector, \(\sigma(i)\in\{i,i+2\}\) in unwrapped integer coordinates. The selected indices for adjacent outputs lie in the common integer arc \([i,i+3]\). Therefore
\[
 |h_{\sigma(i+1)}-h_{\sigma(i)}|
 \le |h_{i+1}-h_i|+|h_{i+2}-h_{i+1}|+|h_{i+3}-h_{i+2}|.
\]
Summation modulo \(n\) gives \(V_n(h\circ\sigma)\le3V_n(h)\). For every cyclic real vector \(w\), the layer-cake representation of its level sets gives
\[
 V_n(w)\le2\lfloor n/2\rfloor\operatorname{osc}(w),
 \qquad V_n(w)\ge2\operatorname{osc}(w),
\]
where \(\operatorname{osc}(w)=\max_i w_i-\min_i w_i\). Since a selector cannot enlarge oscillation, its variation norm is also bounded by \(\lfloor n/2\rfloor\). Hence \(n=4,5\) have the upper bound \(2\), while \(n\ge6\) have upper bound \(3\). For \(n=3\), \(\{i,i+2\}=\{i-1,i\}\) is a consecutive two-point window up to shift, and Step 2 gives upper bound \(1\).

**4. Exact attaining pairs.** For each \(n\), choose the real base vector \(b\) and Boolean perturbation \(h\) as follows. All listed base vectors have strict, unambiguous two-tap comparisons.

- \(n=3\): \(b=(0,1,2)\), \(h=(0,1,0)\), and the selected perturbation is \((0,1,0)\).
- \(n=4\): \(b=(0,1,2,3)\), \(h=(0,0,0,1)\), and the selected perturbation is \((0,1,0,1)\).
- \(n=5\): \(b=(0,1,2,3,4)\), \(h=(0,0,0,0,1)\), and the selected perturbation is \((0,0,1,0,1)\).
- Every \(n\ge6\): let \(b=(0,3,1,2,4,5,b_6,\ldots,b_{n-1})\), where \(b_i=-10-i\) for \(6\le i<n\), and let \(h_i=1\) precisely for \(i\in\{2,3,4\}\), zero otherwise. The selected perturbation is \((1,0,1,0,1,0,\ldots,0)\).

The displayed selected perturbations have variation, respectively, \(2,4,4,6\), while every \(h\) has variation \(2\). For \(0<\varepsilon<1/4\), comparisons stay unchanged along the pair \(b,b+\varepsilon h\), so those two actual inputs attain the factors \(1,2,2,3\).

**5. Sharp one-input gapped factor.** Let \(u_i=x_i\) and \(v_i=x_{i+2}\). The elementary sorting inequality
\[
 |\max(a,b)-\max(c,d)|+|\min(a,b)-\min(c,d)|\le|a-c|+|b-d|
\]
implies, after summing adjacent output differences, \(V_n(G_nx)\le V_n(u)+V_n(v)=2V_n(x)\). For \(n=3\), Step 2 improves this bound to one. For \(n\ge4\), take \(x=e_0\): the dilation is the indicator of the two nonadjacent sites \(0\) and \(n-2\), giving \(V_n(G_ne_0)=4\) and \(V_n(e_0)=2\). All stated bounds are sharp.

## Verification

The accompanying standalone script `verify.py` uses only Python's standard library. It exhaustively compares strict-order selector patterns against every nontrivial cyclic-interval indicator for sizes \(3\le n\le7\), tests the explicit attaining data through \(n=100\), and independently runs seeded random two-input checks. Its finite computations are regression checks only; the proof above establishes the results for every admissible dimension and signal.

## Relationship to prior work

Classical mathematical morphology already defines flat grey-scale dilation by pointwise maxima over translated structuring elements; see Maragos–Schafer and Heijmans. Neither this terminology nor the general maximum-selector representation is claimed as new. In the inspected sections of these primary treatments, the established results concern lattice structure, dilation/erosion representations, threshold sets, and composition, rather than the exact *two-input* cyclic bounded-variation operator constants and the contiguous-versus-gapped distinction given here. Aldaz–Pérez Lázaro studies bounded-variation contraction for the *averaged, noncentered Hardy–Littlewood maximal operator*, a different one-input nonlinear map; its theorem does not imply these two-input statements. Published calculations of variation for graph averaging maximal operators likewise do not determine perturbation norms of local flat dilations. An equivalent historical result under alternative image-processing terminology remains possible.

## Limitations

The exact gapped-window classification is for the two-tap set \(\{0,2\}\), not arbitrary disconnected windows. The interval result covers all nonempty consecutive windows. No analogous assertion is made for weighted variations, noncyclic endpoints, nonflat structuring functions, iterated nonlinear filters, or higher-dimensional grid images. Neither an independent audit nor an exhaustive historical-literature uniqueness claim is asserted.

## References

1. P. Maragos and R. W. Schafer, *Morphological Filters—Part I: Their Set-Theoretic Analysis and Relations to Linear Shift-Invariant Filters*, IEEE Transactions on Acoustics, Speech, and Signal Processing **35** (1987), 1153–1169, doi:10.1109/TASSP.1987.1165259; author-hosted open PDF: https://robotics.ntua.gr/wp-content/uploads/publications/1987_MaragosSchafer_MorphologicFilters-part1_ieeetASSP_%2Bcorrections1989.pdf.
2. H. J. A. M. Heijmans, *Mathematical Morphology: A Modern Approach in Image Processing Based on Algebra and Geometry*, SIAM Review **37** (1995), 1–36, https://ir.cwi.nl/pub/2230/2230D.pdf; particularly §6 on flat grey-scale operations.
3. J. M. Aldaz and J. Pérez Lázaro, *Functions of bounded variation, the derivative of the one dimensional maximal function, and applications to inequalities*, arXiv:math/0601044 (first version 2006-01-03), https://arxiv.org/abs/math/0601044.
