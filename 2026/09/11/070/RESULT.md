# Corrected 1+1+1+1 Star Quintic Contribution at Weights (0,1,3,7,11): Target Value Disproved

## Context

Let $X\subset\mathbf{P}^4$ be the quintic threefold with the standard torus
$T=(\mathbf{C}^*)^5$ acting diagonally with weights
$\lambda^\dagger=(0,1,3,7,11)$. Consider genus-$0$ degree-$4$ stable maps to
$\mathbf{P}^4$ with the quintic Euler-class twist. Among the $T$-fixed loci,
the $1{+}1{+}1{+}1$ stars consist of a contracted genus-$0$ central component
over a fixed point $p_k$ carrying four nodes, joined to four degree-$1$ tails
ending at fixed points $q_a\ne k$. Each such fixed locus is isomorphic to
$\bar M_{0,4}$ (dimension one), and the contribution involves
$\psi$-classes at the four central half-edges. The admitted target claim was

$$S_\star(\lambda^\dagger)=\frac{589731482057}{6}\quad\text{exactly over }\mathbf{Q},$$

with $1/|\mathrm{Aut}|$ tail-permutation weights and the $\bar M_{0,4}$
integral of $\prod_{a=1}^4 1/(w_a-\psi_a)$ included, where
$w_a=\lambda_k-\lambda_{q_a}$.

## Definitions

- $e(T_{p_k})=\prod_{j\ne k}(\lambda_k-\lambda_j)$.
- Flag weights $w_a=\lambda_k-\lambda_{q_a}\ne 0$ (weights are distinct, so all
  star denominators are nonzero).
- $\bar M_{0,4}$ integral ($e_F=\psi_a$ at the central end):
  $$\int_{\bar M_{0,4}}\prod_{a=1}^4\frac{1}{w_a-\psi_a}
    =\frac{\sum_a 1/w_a}{\prod_a w_a},$$
  since $\dim\bar M_{0,4}=1$ and $\int_{\bar M_{0,4}}\psi_a=1$.
- $\mathbf{P}^4$ virtual-normal factor per ordered star (Graber-Pandharipande
  Section 4 assembly; $d=1$ edge factors):
  $$N_{\mathbf{P}^4}=\frac{1}{e(T_{p_k})\prod_a e(T_{q_a})}
    \prod_a\frac{1}{(-w_a)}\cdot J,\qquad
    J=\frac{\sum_a 1/w_a}{\prod_a w_a}.$$
- Quintic twist from the normalization sequence
  $0\to\mathcal{O}_C\to\mathcal{O}_{C_0}\oplus\bigoplus_e\mathcal{O}_{C_e}
  \to\bigoplus_{\mathrm{nodes}}\mathcal{O}_x\to 0$ twisted by
  $f^*\mathcal{O}(5)$ (genus $0$, tree, so $H^1=0$):
  $$Q=\frac{\prod_a Q(k,q_a)}{(5\lambda_k)^3},\qquad
    Q(k,q)=\prod_{m=0}^5\big((5-m)\lambda_k+m\lambda_q\big).$$
- $1/|\mathrm{Aut}|$ via ordered labels summed then divided by $24$
  (orbit-stabilizer), independently re-summed over multisets with
  $1/|\mathrm{Stab}|$.

## Result

At $\lambda^\dagger=(0,1,3,7,11)$, with the standard localization data above,

$$S_\star(\lambda^\dagger)=
\frac{14339846746454566537552143617879921875}{1033947715493982426365952}
\approx 1.3869025030539\times 10^{10},$$

in lowest terms (numerator odd, denominator $2^{56}\cdot 3^{15}$). Hence, with
$T=589731482057/6$,

$$S_\star(\lambda^\dagger)-T=
\frac{14238221493349947264524492660279301331}{1033947715493982426365952}
\ne 0,$$

so the target equality $S_\star(\lambda^\dagger)=589731482057/6$ is disproved.
Per-central-point sectors ($\times 1/24$): $k=0$: $0$;
$k=1$ ($\lambda=1$): $9491579642797890625/30091839012864$;
$k=3$: $-712067344269069671630859375/288230376151711744$;
$k=7$: $105666361664708414601898193359375/126214320739011526656$;
$k=11$: $3756880418165438090995129921875/288230376151711744$.
Of $5\times 4^4=1280$ ordered stars ($4^4=256$ in the $k=0$ block, vanishing
in the limit), $306$ are individually nonzero.

## Proof / Evidence

Exact `Fraction` arithmetic over all ordered stars gives the total above; an
independent code path summing over unordered multisets with $1/|\mathrm{Stab}|$
agrees exactly. A sample check gives $J=-7/3600$ for
$(k,q)=(1,(0,2,3,4))$. The true denominator $2^{56}\cdot 3^{15}$ retains the
full edge-weight prime content (powers of $2$ from even weight differences,
$3^{15}$ from weights divisible by $3$), which no $S_4$ automorphism order
$24=2^3\cdot 3$ can cancel to $6$; the target's denominator $6$ was wishful
cancellation. A robustness sweep (alternative $J_{\mathrm{alt}}=1/\sum w$,
omitted/extra node subtractions, dropped central $H^0$ factor, truncated
edge-weight ranges, divisions by $1$, $6$, $24$) never reproduces the target.
Dropping the quintic twist, the pure-$\mathbf{P}^4$ star sum is
$\approx -3.7\times 10^{-12}$ (essentially $0$), the expected residue
cancellation, confirming the assembly is implemented correctly and the nonzero
quintic total is genuine twist content.

## Limitations

The disproof is relative to the standard Graber-Pandharipande Section 4
contracted-vertex, edge, and quintic-twist data stated above; an intentionally
nonstandard vertex convention could define a different sum, but no such reading
among those swept reproduces the target. The $k=0$ sector is evaluated as the
limit $0$ (each $Q(0,q)$ carries a factor $5\lambda_0=0$ per edge, four zeros,
against $(5\lambda_0)^3$ in the denominator). No claim is made about other
graph topologies, other weights, or the full degree-$4$ quintic number.

## Reproducibility

Run `python3 output/artifacts/star_sum.py` (exact arithmetic; prints total,
per-sector values, sample $J$, variant sweeps) and
`python3 output/artifacts/verify_and_sweep.py` (multiset $1/|\mathrm{Stab}|$
re-sum plus diagnosis sweep). Both use only the Python standard library.

## References

- T. Graber and R. Pandharipande, "Localization of virtual classes",
  arXiv:alg-geom/9708001, Sections 1-4.
- M. Kontsevich, "Enumeration of rational curves via torus actions":
  graph-sum ancestor of the Section 4 formula.
- R. Pandharipande and A. Pixton, "Gromov-Witten/Pairs correspondence for the
  quintic 3-fold": capped localization context (no isolated star residue).
