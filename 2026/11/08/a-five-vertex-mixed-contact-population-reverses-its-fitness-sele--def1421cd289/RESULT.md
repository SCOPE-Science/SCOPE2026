# A five-vertex mixed-contact population reverses its fitness-selection effect

## Finding

A population with five individuals and just four contacts, three dyadic and one triadic, can promote beneficial mutations under weak selection but suppress those same mutations at a higher fitness. Specifically, for the full-group copying birth–death process defined below, if \(\rho_H(r)\) is the fixation probability from one uniformly placed mutant and \(\rho_M(r)=(1-r^{-1})/(1-r^{-5})\) is the five-individual Moran benchmark (with continuous value \(1/5\) at \(r=1\)), then

\[
\rho_H(1)=\frac15,\qquad
\rho_H'(1)-\rho_M'(1)=\frac{10}{993}>0.
\]

Consequently \(\rho_H(r)>\rho_M(r)\) for all \(r>1\) sufficiently close to one. More concretely,

\[
\begin{aligned}
\rho_H(3/2)&=\frac{117586744909890489}{305499880204846910}
>\frac{81}{211}=\rho_M(3/2),\\
\rho_H(2)&=\frac{48223659521389}{94272370085844}
<\frac{16}{31}=\rho_M(2).
\end{aligned}
\]

Continuity therefore ensures at least one amplification-to-suppression crossover \(r_*\in(3/2,2)\). No uniqueness or complete all-fitness classification is asserted.

## Assumptions and scope

The population has vertex set \(V=\{0,1,2,3,4\}\), with distinct undirected hyperedges

\[
E=\bigl\{\{0,1\},\{0,2\},\{0,3\},\{0,1,4\}\bigr\}.
\]

These four contacts are individually sampled units; pair \(\{0,1\}\) and triple \(\{0,1,4\}\) both appear, as allowed in a general hypergraph where different group sizes may coexist. The contact-incidence degrees of vertices \(0,1,2,3,4\) are \((4,2,1,1,1)\). This hypergraph is connected.

Each vertex contains either a mutant, of relative fitness \(r>0\), or a resident, of fitness one. At each discrete update, one parent is sampled in proportion to its individual fitness; it selects one of the hyperedges containing it uniformly; *every other vertex in that hyperedge* immediately adopts the parent's type. Updates continue to fixation or extinction. The initial mutant is uniformly chosen among the five vertices. No mutation occurs subsequently. This is full-hyperedge-copying model 1, not majority-gated copying, a death–Birth process, or a pairwise one-mode projection.

## Proof

For a current mutant set \(S\subseteq V\), let \(m=|S|\) and let \(d_u\) be the number of hyperedges incident to vertex \(u\). For every parent \(u\) and incident hyperedge \(e\), define

\[
T_{u,e}(S)=
\begin{cases}
S\cup e,&u\in S,\\
S\setminus e,&u\notin S.
\end{cases}
\]

The probability of this particular parent-and-contact choice is

\[
q_{u,e}(S;r)=
\frac{r^{\mathbf1_{u\in S}}}{(5+(r-1)m)d_u}.
\]

Sum over all choices producing a given target to obtain a row-stochastic transition matrix \(P(r)\) on the \(32\) mutant subsets. With \(f_{\varnothing}(r)=0\), \(f_V(r)=1\), the \(30\) interior fixation probabilities satisfy the exact finite system

\[
 f_S(r)=\sum_{u\in V}\sum_{e\ni u}q_{u,e}(S;r)f_{T_{u,e}(S)}(r),
\quad\varnothing\ne S\ne V. 
\]

Every mixed state can reach all-mutant fixation through a finite sequence of positive-probability choices: repeatedly use a mutant parent in a hyperedge meeting the currently resident set. Connectedness guarantees a boundary hyperedge until every site is mutant. Hence no nonabsorbing closed class exists; the finite chain is absorbed almost surely and its transient matrix \(I-Q(r)\) is nonsingular for every \(r>0\).

Solving this rational system at \(r=3/2\) and \(r=2\), then averaging the five singleton entries, gives the displayed exact fractions. Their differences from the Moran baseline are exactly

\[
\rho_H(3/2)-\rho_M(3/2)=
\frac{65312879394293469}{64460474723222698010}>0
\]

and

\[
\rho_H(2)-\rho_M(2)=
-\frac{13424476210445}{2922443472661164}<0.
\]

At neutrality, the vector with vertex weights proportional to \(d_u^{-1}\) is harmonic: for each oriented pair of vertices inside a chosen hyperedge, the neutrality drift of \(\sum_{u\in S}d_u^{-1}\) cancels its opposite ordered contribution. The singleton fixation probabilities are therefore \(1/15,2/15,4/15,4/15,4/15\) and their average is \(1/5\).

To differentiate the finite linear system, write \(A(r)f(r)=b(r)\), where \(A=I-Q\). At neutrality,

\[
 A(1)f'(1)=b'(1)-A'(1)f(1).
\]

The derivative of the parent-and-contact probability at \(r=1\) is explicitly

\[
 q'_{u,e}(S;1)=\frac{5\mathbf1_{u\in S}-|S|}{25d_u}.
\]

The same exact rational elimination returns

\[
\bigl(f_{\{0\}}'(1),f_{\{1\}}'(1),f_{\{2\}}'(1),f_{\{3\}}'(1),f_{\{4\}}'(1)\bigr)
=\left(\frac{1398}{8275},\frac{2474}{8275},\frac{13412}{24825},\frac{13412}{24825},\frac{2492}{4965}\right).
\]

Consequently \(\rho_H'(1)=2036/4965\). The five-vertex Moran derivative is \(\rho_M'(1)=2/5\), and their difference is \(10/993\). Since the rational Markov solution is analytic on \(r>0\), the positive derivative difference yields a genuine open interval of weak-selection amplification. The opposite signs at \(r=3/2\) and \(r=2\), plus continuity, yield a crossover in the asserted open interval.

## Verification

Run `python verify.py` with Python 3 and its standard library, without external packages. It independently constructs and solves the full \(30\)-transient-state and symmetry-lumped \(22\)-transient-state exact rational backward equations at fitness values \(1,3/2,2\). It checks the full singleton vectors agree across both implementations, verifies all displayed rational probabilities and gaps, and separately differentiates the unreduced equations at neutrality to check the slope and singleton derivatives. Every elimination result is checked by substitution into its original system. All arithmetic uses Python's exact `fractions.Fraction`, not floating-point convergence tests. The verifying script itself is part of this package.

## Relationship to prior work

Liu and Masuda (2023) define this full-hyperedge copying model and study complete, cyclic and star three-uniform hypergraphs plus several empirical hypergraphs, finding suppression in their investigated examples. Their neutral-drift theorem gives uniform-initialization probability \(1/N\) and does not derive the mixed-size five-site regime reversal here. The present finding neither contests their reported observations nor claims that all hypergraphs behave alike.

Alcalde Cuesta, González Sequeiros and Lozano Rojo (2018) demonstrate fitness-dependent evolutionary regimes for ordinary dyadic graphs; Bhaumik and Masuda (2024) likewise examine weighted dyadic networks and transient amplification. These establish that regime reversal itself is not unprecedented in evolutionary population models. The 2018 census finds such amplifier-to-suppressor transitions for unweighted ordinary graphs starting at seven vertices, whereas this mixed-contact example uses five; this comparison does not assert global minimality for hypergraphs or weighted graphs. However, their dynamics replace **one neighbor per event**, whereas the hyperedge \(\{0,1,4\}\) here allows two concurrent replacements. The graph theorems and graphs enumerated there do not imply the exact fixation identities or the weak-selection derivative in this particular mixed-group copying process. In particular, one-mode projection does not preserve the full-group update rule.

## Limitations

This is one explicit finite, connected, mixed-size hypergraph. It demonstrates a local amplification-to-suppression reversal, not a complete classification of all five-site hypergraphs, all fitness regimes, or all mutation placements. A crossing exists somewhere between \(3/2\) and \(2\); uniqueness and exact location are not proved. Small-population exactness is mathematical, not a claim of empirical biological predictive validity. Priority against every unindexed publication remains unverified; independent audit has not been performed.

## References

1. Liu, R., and Masuda, N. (2023), *Fixation dynamics on hypergraphs*, PLOS Computational Biology 19:e1011494, https://doi.org/10.1371/journal.pcbi.1011494 ; earliest public preprint https://arxiv.org/abs/2301.05343 (January 13, 2023).
2. Alcalde Cuesta, F., González Sequeiros, P., and Lozano Rojo, Á. (2018), *Evolutionary regime transitions in structured populations*, PLOS ONE 13:e0200670, https://doi.org/10.1371/journal.pone.0200670 .
3. Bhaumik, J., and Masuda, N. (2024), *Constant-selection evolutionary dynamics on weighted networks*, Proceedings of the Royal Society A 480:20240223, https://arxiv.org/abs/2403.17208 .
