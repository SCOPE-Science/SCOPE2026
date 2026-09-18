# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The main estimate is based on a binary gap decomposition that is specific to the ordered real line.
For every \(c_0<c\), each nontrivial compact node of diameter \(d\) contains a gap longer than
\(c_0d\). Removing that gap leaves two children whose diameters have sum \(<(1-c_0)d\).
At depth \(k\), the sum of active diameters is therefore at most
\((1-c_0)^k d\), while the number of active nodes is at most \(2^k\). For target scale \(r\),
this gives
\[
I_k\le\min\{2^k,(d/r)(1-c_0)^k\}.
\]
Summing at the crossover produces exponent
\[
s_0=\frac{\log2}{\log(2/(1-c_0))}.
\]
The stopped binary tree has one more leaf than internal node, and each leaf has diameter at most
\(r\), yielding the Assouad covering estimate. Letting \(c_0\uparrow c\) gives the claimed
\(\Phi(c)\).

The closure step was checked separately: a violating finite chain in the closure has a strict
step-size margin and can be approximated vertex-by-vertex by a violating chain in the original
set. Subsets inherit the chain condition.

Sharpness was checked directly for the symmetric two-branch central Cantor set with contraction
\(q=(1-c)/2\). The first common ancestor of any distinct pair supplies a separating gap of
relative size at least \(c\), while the endpoint pair \(0,1\) has largest gap exactly \(c\).
Strong separation gives Assouad dimension \(\log2/(-\log q)\), matching the upper bound.

The clock realization was also checked directly. In the pure-jump clock
\[
g_c(t)=\sum_{\tau_G<t}|G|,
\]
where \(\tau_G\) is the midpoint of each complementary gap \(G\) of the central Cantor set,
the total gap length to the left of a Cantor point \(t\) equals \(t\), because the Cantor set has
Lebesgue measure zero. Across a gap \((a,b)\), the clock takes the endpoint values \(a\) and
\(b\). Hence its image is exactly the Cantor set. The published bottleneck--jump identity then
gives \(\kappa_{g_c}=c\).

No computation is required for the proof.

## Originality

The motivating preprint arXiv:2609.20706v1 was inspected through its theorem statements and
proofs on uniform disconnectedness, the real-line gap identity, exact identification of the
optimal constant with \(\kappa_g\), examples, and structural consequences. Its full searchable
HTML contains no occurrence of “Assouad”, “dimension”, or “porous”. It therefore does not state
the dimension ceiling, its sharpness, the Cantor clock extremizers, or the Assouad-dimension
selection criterion.

The following neighboring literature was checked for coverage or stronger implications:

- Mackay--Tyson, *Conformal Dimension: Theory and Application* (2010): standard implication
  \(\dim_A X<1\Rightarrow X\) uniformly disconnected.
- Luukkainen (1998): classical quantitative relationship between porosity and non-full Assouad
  dimension in Euclidean spaces.
- Fraser--Henderson--Olson--Robinson (2015): Assouad dimension of self-similar sets on the line;
  in particular, separated self-similar sets have the expected similarity dimension.
- Chrontsios Garitsis--Tyson (2023): explicitly describes the general porosity/Assouad
  quantitative conversion as non-sharp in the quasisymmetric-distortion setting.
- Recent work on uniformly disconnected sets and Cantor geometry was searched using combinations
  of “uniform disconnectedness constant”, “chain”, “largest gap”, “Assouad dimension”, “sharp
  bound”, “Cantor”, and the explicit expression \(\log2/\log(2/(1-c))\).

These searches found the qualitative equivalences and general porosity estimates, but no sharp
extremal theorem for the optimal chain constant
\[
c_*(D)=\inf_{u<v}\Gamma_D(u,v)/(v-u),
\]
no matching central-Cantor extremal statement, and no Stieltjes-clock transfer with equality.

The most plausible residual coverage risks are the full text of David--Semmes,
*Fractured Fractals and Broken Dreams* (1997), and Luukkainen (1998), both of which develop
quantitative uniform disconnectedness/porosity theory. Their relevant bibliographic and
secondary descriptions were inspected, but a complete theorem-by-theorem full-text comparison
was not performed. No concrete evidence was found that either contains the stated sharp
one-dimensional function \(\Phi(c)\). Because the motivating Stieltjes-clock preprint is very
recent, unindexed parallel work is also a residual originality risk.

Originality is therefore assessed to the best of current knowledge, not as an exhaustive
literature guarantee.

## Value

The result replaces a qualitative “dimension is below one” consequence by the exact extremal
tradeoff between a natural chain-separation constant and Assouad dimension on the line.
It is sharp for every parameter value, identifies explicit extremizers, and converts the new
Stieltjes jump-dominance invariant into a sharp fractal-dimension constraint. The corollary
\[
\text{universal Hölder selection}\iff \dim_A\operatorname{Im}(g)<1
\]
also gives a dimension-theoretic interpretation of the recent clock-selection criterion.

## Limitations

The sharp formula uses one-dimensional order and does not claim an analogue with the same
constant in higher-dimensional Euclidean spaces or general metric spaces. The Assouad-dimension
value alone does not quantitatively determine \(\kappa_g\). The central-Cantor examples establish
sharpness of the upper envelope but do not classify all extremizers.
