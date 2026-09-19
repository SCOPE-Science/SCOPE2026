# Minimal branching degree is upper semicontinuous with saturated parity spectrum

Let \(S\) be a closed oriented surface of genus \(g\ge 2\), and let
\[
\mathfrak X_3(S)
=
\mathrm{Hom}^{+}\!\bigl(\pi_1(S),\mathrm{PSL}(3,\mathbb R)\bigr)
/\mathrm{PSL}(3,\mathbb R)
\]
be the real projective character variety. For a signature
\(\mu=(m_1,\dots,m_k)\) of positive branch orders, write
\(\deg\mu=\sum_i m_i\), and also allow the empty signature of degree \(0\).
Define the total-degree realization spectrum of a representation \(\rho\) by
\[
\mathcal D(\rho)
=
\left\{
\deg\mu:
\rho\in
\operatorname{hol}\bigl(\mathcal{RP}^2(\mu)\bigr)
\right\},
\]
and define its minimal branching degree
\[
d(\rho)=\min \mathcal D(\rho).
\]

Faraco--Rungi prove that every representation is geometrizable by a branched
real projective structure, so \(d(\rho)\) is finite. They also prove that the
holonomy image of every fixed signature is open, that every realization obeys
\[
\deg\mu\equiv w_2(\rho)\pmod 2,
\]
and that bubbling preserves holonomy while increasing total branching degree
by \(2\).

These ingredients imply the following global structure theorem.

## Theorem

For every \(\rho\in\mathfrak X_3(S)\):

1. **Saturated parity ray.**
   \[
   \boxed{
   \mathcal D(\rho)
   =
   d(\rho)+2\mathbb Z_{\ge0}.
   }
   \]
   In particular,
   \[
   d(\rho)\equiv w_2(\rho)\pmod2.
   \]

2. **Open exact-degree loci.** For every \(m\ge0\),
   \[
   \mathcal R_m
   :=
   \{\rho:m\in\mathcal D(\rho)\}
   \]
   is open in \(\mathfrak X_3(S)\).

3. **Upper semicontinuity of minimal degree.** For every \(m\ge0\),
   \[
   \mathcal U_m
   :=
   \{\rho:d(\rho)\le m\}
   \]
   is open. Equivalently,
   \[
   \rho_j\to\rho
   \quad\Longrightarrow\quad
   \limsup_{j\to\infty}d(\rho_j)\le d(\rho).
   \]

4. **Generic local constancy without a Baire hypothesis.** The locus
   \[
   \mathcal L
   :=
   \{\rho:d\text{ is locally constant at }\rho\}
   \]
   is open and dense. Its complement
   \[
   \mathcal J:=\mathfrak X_3(S)\setminus\mathcal L
   \]
   is closed and nowhere dense, and more precisely
   \[
   \boxed{
   \mathcal J
   =
   \bigcup_{m\ge0}\partial\mathcal U_m.
   }
   \]
   Consequently the full degree spectrum \(\mathcal D(\rho)\), not only its
   minimum, is locally constant on the open dense set \(\mathcal L\).

5. **Finite branch-data banks on compact families.** For every compact
   \(K\subset\mathfrak X_3(S)\), there exist finitely many signatures
   \(\mu_1,\dots,\mu_N\) such that every \(\rho\in K\) is realized in at least
   one of the strata \(\mathcal{RP}^2(\mu_i)\). In particular,
   \[
   \sup_{\rho\in K}d(\rho)<\infty.
   \]

Thus the unresolved problem of computing \(d(\rho)\) for non-Hitchin
representations carries a rigid topological envelope: total branching degrees
never occur sporadically, minimal degree can jump only upward under
specialization, and all such jumps are confined to a closed nowhere-dense
subset of the character variety.

## Proof

### 1. Saturation of the total-degree spectrum

By the geometrization theorem of Faraco--Rungi,
\(\mathcal D(\rho)\neq\varnothing\). Since it is a nonempty subset of
\(\mathbb Z_{\ge0}\), it has a minimum \(d(\rho)\).

Their Stiefel--Whitney obstruction says that every
\(m\in\mathcal D(\rho)\) satisfies
\[
m\equiv w_2(\rho)\pmod2.
\]
Hence every realized degree has the same parity as \(d(\rho)\), and no
integer of the opposite parity can occur.

Choose a realization of \(\rho\) of total degree \(d(\rho)\).
Faraco--Rungi's bubbling surgery is available for an arbitrary possibly
branched real projective structure; each bubble leaves the holonomy unchanged
and raises the total branching degree by \(2\). Iterating gives realizations
of degrees
\[
d(\rho),\ d(\rho)+2,\ d(\rho)+4,\dots.
\]
Minimality excludes smaller degrees, and the parity obstruction excludes every
remaining integer. Therefore
\[
\mathcal D(\rho)=d(\rho)+2\mathbb Z_{\ge0}.
\]

### 2. Openness of exact-degree and sublevel loci

Fix \(m\ge0\). There are only finitely many signatures of total degree \(m\):
they are precisely the integer partitions of \(m\), with the empty signature
when \(m=0\). For each fixed signature \(\mu\), Faraco--Rungi's stratified
Ehresmann--Thurston principle states that
\[
\operatorname{hol}\bigl(\mathcal{RP}^2(\mu)\bigr)
\]
is open in \(\mathfrak X_3(S)\). Hence the finite union
\[
\mathcal R_m
=
\bigcup_{\deg\mu=m}
\operatorname{hol}\bigl(\mathcal{RP}^2(\mu)\bigr)
\]
is open.

Similarly,
\[
\mathcal U_m
=
\bigcup_{r=0}^{m}\mathcal R_r
\]
is open. This is exactly upper semicontinuity of the integer-valued function
\(d\).

Using the saturated-spectrum formula one may equivalently write
\[
\mathcal R_m
=
\left\{
\rho:
d(\rho)\le m,\quad
d(\rho)\equiv m\pmod2
\right\}.
\]

### 3. The locally constant locus is open dense

Openness of \(\mathcal L\) is immediate from its definition. To prove density,
let \(O\subset\mathfrak X_3(S)\) be any nonempty open set. The nonempty subset
\(d(O)\subset\mathbb Z_{\ge0}\) has a least element; call it \(m\), and choose
\(\rho\in O\) with \(d(\rho)=m\). Since \(\mathcal U_m\) is open,
\[
O\cap\mathcal U_m
\]
is a nonempty open neighborhood of \(\rho\). By minimality of \(m\) on \(O\),
every point of this intersection has minimal degree exactly \(m\). Thus every
nonempty open set contains a nonempty open subset on which \(d\) is constant.
Therefore \(\mathcal L\) is dense.

It remains to identify the jump locus. If
\(\rho\in\partial\mathcal U_m\), then \(\rho\notin\mathcal U_m\) because
\(\mathcal U_m\) is open, while every neighborhood of \(\rho\) meets
\(\mathcal U_m\); hence \(d\) cannot be locally constant at \(\rho\).

Conversely, suppose \(d\) is not locally constant at \(\rho\), and put
\(r=d(\rho)\). The open set \(\mathcal U_r\) is a neighborhood of \(\rho\).
Inside this neighborhood all values are at most \(r\); failure of local
constancy therefore means that every neighborhood of \(\rho\) contains a
point of degree at most \(r-1\). Hence
\[
\rho\in\partial\mathcal U_{r-1}.
\]
(The case \(r=0\) cannot occur, since \(\mathcal U_0\) itself is an open
degree-zero neighborhood.) This proves
\[
\mathcal J=\bigcup_{m\ge0}\partial\mathcal U_m.
\]
Since \(\mathcal L\) is open dense, \(\mathcal J\) is closed nowhere dense.

The saturated-spectrum formula shows that local constancy of \(d\) is
equivalent to local constancy of the entire set \(\mathcal D(\rho)\).

### 4. Compact families admit finitely many fixed signatures

For each \(\rho\in K\), choose a signature \(\mu_\rho\) realizing
\(d(\rho)\). The open sets
\[
\operatorname{hol}\bigl(\mathcal{RP}^2(\mu_\rho)\bigr)
\]
cover \(K\). Compactness provides a finite subcover, say from
\(\mu_1,\dots,\mu_N\). Every representation in \(K\) is therefore realized
by one of these finitely many branch patterns, and
\[
d(\rho)\le\max_i\deg\mu_i
\]
on \(K\).

## Consequences and interpretation

For a Hitchin representation, the Choi--Goldman unbranched convex structure
gives \(d(\rho)=0\); the theorem then recovers
\[
\mathcal D(\rho)=2\mathbb Z_{\ge0}
\]
at the level of total degree. Faraco--Rungi prove the stronger Hitchin
statement that every *signature* of even degree is realizable.

For a general non-Hitchin representation, prescribed-signature realization
remains substantially finer than total-degree realization. The theorem does
not compute the unknown number \(d(\rho)\), but once that one integer is
known, it completely determines which total branching degrees can occur.

Upper semicontinuity has a useful geometric direction: if a representation
admits a realization with small total branching degree, then all sufficiently
nearby representations admit a realization with no larger degree. Higher
minimal branching complexity can therefore appear only as an upward jump at a
special limiting representation. The theorem shows that these jump points
form a closed nowhere-dense set.

## Relation to prior literature

Faraco--Rungi, *Branched real projective structures on surfaces and
geometrisation of representations* (arXiv:2609.18436, submitted 16 September
2026), provide the four inputs used above: global geometrizability, openness
of the holonomy image of each signature stratum (Proposition 2.13), the
Stiefel--Whitney parity obstruction (Corollary 4.6), and holonomy-preserving
bubbling that adds two to the branch degree (Remarks 4.8--4.9 and Proposition
4.11). Their Problem 1.4 asks for the minimal branching degree of a
non-Hitchin representation.

In the complex-projective \(\mathrm{PSL}(2,\mathbb C)\) setting, Thomas Le
Fils, *Holonomy of complex projective structures on surfaces with prescribed
branch data*, Journal of Topology 16 (2023), 430--487,
doi:10.1112/topo.12287, computes an analogous minimal degree \(d(\rho)\) and
uses degree-raising surgeries. This is important neighboring precedent.
No statement matching the upper-semicontinuity theorem, the open-dense local
constancy result, the closed nowhere-dense jump locus, or the compact
finite-signature-bank consequence was located there.

The contribution claimed here is therefore not any of the four
Faraco--Rungi ingredients, nor the notion of minimal branching degree. It is
the structural theorem obtained by combining the fixed-stratum deformation
principle with parity and bubbling: the saturated parity-ray spectrum and the
topology of the resulting minimal-degree function.

## Limitations

- The theorem does **not** compute \(d(\rho)\) for non-Hitchin
  representations and therefore does not solve Faraco--Rungi Problem 1.4.
- It classifies realizable **total degrees**, not realizable individual
  signatures. Distinct branch partitions of the same degree can behave
  differently.
- No explicit upper bound for \(d(\rho)\), no quantitative neighborhood size,
  and no description of the closed nowhere-dense jump locus are obtained.
- The compact-family statement is qualitative: it produces a finite
  signature bank but no effective bound on its size or degrees.
- The main source is a very recent preprint. Later revisions or unindexed
  parallel observations may overlap with these structural consequences.

## References

1. G. Faraco and N. Rungi, *Branched real projective structures on surfaces
   and geometrisation of representations*, arXiv:2609.18436 (2026).
   https://arxiv.org/abs/2609.18436
2. T. Le Fils, *Holonomy of complex projective structures on surfaces with
   prescribed branch data*, Journal of Topology **16** (2023), 430--487.
   https://doi.org/10.1112/topo.12287
