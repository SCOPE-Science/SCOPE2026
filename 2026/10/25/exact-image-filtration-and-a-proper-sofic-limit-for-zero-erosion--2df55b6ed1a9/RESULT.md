# Exact image filtration and a proper sofic limit for zero-erosion cellular automata

## Finding

For every integer \(r\ge2\), the unique-active-transition automaton \(T_r\) has a complete and explicit filtration of its images. Set \(\Sigma=\{0,1\}^{\mathbb Z}\). Its local rule changes \(x_i=0\) to \(1\) exactly when
\[
  x_{i-r+1}=\cdots=x_i=0,\qquad x_{i+1}=1,
\]
and leaves all other symbols unchanged. For each \(n\ge0\) write \(\mathcal I_n=T_r^n(\Sigma)\). Then
\[
\boxed{\mathcal I_n=\bigl\{y\in\Sigma:\text{no word }0^r1^j0\text{ occurs in }y\text{ for }1\le j\le n\bigr\}.}
\]
For \(n=0\), the empty list of forbidden words means the full shift. In particular each \(\mathcal I_n\) is a shift of finite type, while \(\mathcal I_{n+1}\subsetneq\mathcal I_n\) for every finite \(n\).

The maximal limit set is
\[
\boxed{\Omega_r=\bigcap_{n\ge0}\mathcal I_n
 =\bigl\{y:\text{no word }0^r1^j0\text{ occurs for any }j\ge1\bigr\}.}
\]
It is a sofic shift that is **not** a shift of finite type. It properly contains the pointwise fixed-point set \(\mathrm{Fix}(T_r)=\{y:0^r1\text{ does not occur}\}\). Thus no finite iterate reaches the limit set, despite every finite iterate having an SFT image.

The sharp backward-depth of \(y\), defined as \(d(y)=\sup\{n\ge0:y\in T_r^n(\Sigma)\}\), is
\[
 d(y)=\min\{j\ge1:0^r1^j0\text{ occurs in }y\}-1,
\]
where the minimum of the empty set is interpreted as infinity.

## Assumptions and scope

The alphabet is binary, the lattice is \(\mathbb Z\) (no boundary or ring is imposed), the neighborhood is the consecutive interval from \(i-r+1\) to \(i+1\), and time is synchronous. The integer \(r\ge2\) is arbitrary. All claimed equalities hold for **all** bi-infinite configurations and **every** integer \(n\ge0\), with no periodicity or finite-support assumption. The case \(r=1\) is excluded: finite zero runs can disappear entirely there, invalidating the run-label preservation used below. The maximal limit set means the intersection of all finite-time images, not an almost-sure or generic attractor.

## Proof

**1. Run evolution.** Any maximal run of consecutive zeros having a finite right endpoint is followed by a one. If its length is at least \(r\), exactly its rightmost zero changes to one in one step; otherwise no zero in that run changes. A left-infinite zero run with a finite right endpoint behaves analogously. A right-infinite zero run has no right endpoint and does not change. The condition \(r\ge2\) ensures that every zero run retains at least one zero under all iterations. Consequently distinct zero runs never merge or disappear, their left endpoints (when defined) remain fixed, and their right endpoints move left by exactly one at each time while their lengths exceed \(r-1\). The intervening one runs cannot shrink.

**2. Necessity of the forbidden words.** Suppose \(y=T_r^n(x)\). Take a finite zero run in \(y\), or a left-infinite zero run with finite right endpoint, that has at least \(r\) zeros and is followed by a *finite* one run and then another zero. Since it is still active at time \(n\), it must have been active throughout the preceding \(n\) updates; its right endpoint has shifted left \(n\) positions. The following zero run existed in \(x\), because zero runs never disappear, and was separated from the first by at least one one. The final intervening one run therefore has length at least \(n+1\). Every occurrence of \(0^r1^j0\) with \(1\le j\le n\) would contradict that property. Hence \(\mathcal I_n\) is contained in the proposed forbidden-word shift.

**3. Sufficiency by a simultaneous explicit inverse.** Let \(y\) avoid all \(0^r1^j0\) with \(1\le j\le n\). For each zero run of length at least \(r\) **with finite right endpoint**, replace its first \(n\) following ones by zeros; leave everything else unchanged. If another zero run follows, the gap of ones between it and the active zero run has length at least \(n+1\), so this operation leaves at least one separating one. If the trailing one run is right-infinite, the operation remains well-defined. These alterations are therefore disjoint even for infinitely many runs, and never cause zero runs to merge. In the resulting predecessor \(x\), precisely the zero runs that were active in \(y\) are longer by \(n\), with their right endpoints moved \(n\) places right. The other zero runs remain shorter than \(r\) or lack finite right endpoints, so they are stationary. By the run-evolution rule, \(n\) synchronous updates of \(x\) restore \(y\). The construction also covers left-infinite active zero runs, which have well-defined finite right endpoints. This proves the reverse inclusion and the exact image formula.

**4. Strict descent and depth.** The periodic configuration obtained by repeating the word \(0^r1^{n+1}\) has the forbidden-word exponent \(j=n+1\) and no shorter exponent. It lies in \(\mathcal I_n\setminus\mathcal I_{n+1}\). The image formula immediately yields the stated sharp backward-depth expression, including the infinity case.

**5. Sofic but not SFT.** The forbidden language \(\{0^r1^j0:j\ge1\}\) is regular. For completeness, a finite labeled right-resolving presentation uses states \(Z_0,Z_1,\ldots,Z_r,P\): on reading zero, \(Z_k\) goes to \(Z_{\min(k+1,r)}\); on reading one, \(Z_k\) goes to \(Z_0\) for \(k<r\), while \(Z_r\) goes to \(P\); from \(P\), ones return to \(P\) and zeros have no outgoing edge. The label sequences of bi-infinite paths are exactly \(\Omega_r\), proving soficity. To rule out finite type, for any putative maximum forbidden-word length \(L\), choose \(j>L\) and a configuration with a single far-separated pattern \(0^r1^j0\) surrounded by infinite ones. This configuration is excluded from \(\Omega_r\), but all its length-\(L\) blocks occur in configurations of \(\Omega_r\): no block is long enough to capture both the \(0^r\) prefix and the terminal zero, and the short blocks admit infinite-one extensions. Thus no finite collection of forbidden blocks can present \(\Omega_r\).

**6. Strict enlargement of the fixed-point set.** A configuration is fixed exactly when no neighborhood \(0^r1\) appears. The step configuration with zeros on every negative coordinate and ones on every nonnegative coordinate contains \(0^r1\) and hence is not fixed; nevertheless it contains no \(0^r1^j0\), because after its transition to ones no zero ever returns. Hence it belongs to \(\Omega_r\setminus\mathrm{Fix}(T_r)\).

## Verification

Run the included `verify.py` with Python 3 (standard library only). It enumerates all binary configurations on finite cyclic rings for \(2\le r\le5\), ring sizes up to \(12\), and \(1\le n\le4\), comparing the exact iterated images with the predicted finite forbidden-word characterization. It also verifies the strict-descent witnesses and finite automaton acceptance on sampled finite words. All tested cases passed. These are **finite consistency checks**, not proofs of the bi-infinite or arbitrary-parameter assertions; those follow from the run argument above.

## Relationship to prior work

Castillo-Ramirez, Magaña-Chavez and de los Santos Baños (arXiv:2411.03601, first public 2024-11-06, primary MSC 37B15) establish that a unique-active-transition automaton with interval neighborhood is either idempotent or strictly almost equicontinuous, and identify the fixed-point subshift. Their Example 2 explicitly includes the \(r=2\) active word \(001\), but their results do not give the exact \(n\)-th image for all \(n\), the explicit backward-depth obstruction, or a classification of the maximal limit set for all \(r\ge2\). The cited 2015–2016 work by de Oliveira and collaborators develops finite-time process-graph methods for elementary cellular automata and treats several other specific limit graphs; a generic finite-automaton construction does not imply this all-radius forbidden-word identity. Ballier's general results concern *stable* cellular automata, unlike the strictly descending image filtration here.

Ruivo and de Oliveira's 2017 work and Kassardjian, de Oliveira and Ruivo's 2025 work address elementary-automaton limit languages and process graphs; only partial previews/abstracts were accessible for the directly relevant comparisons. They constitute unresolved historical-priority risks, especially for the single elementary case \(r=2\). The present claim includes all \(r\ge2\) and all \(n\), and the precise implications of inaccessible sources were **not** assumed away.

## Limitations

No generalization to arbitrary active words, alphabets, nonsynchronous updates, or higher-dimensional lattices is claimed. The theorem identifies the maximal topological limit set, not its measure-theoretic generic attractor or entropy. The finite-ring verifier does not establish the infinite-lattice theorem. No independent mathematical audit or blanket historical novelty certification has been performed. The two relevant historical process-graph works have unresolved full-text comparison risk.

## References

1. A. Castillo-Ramirez, M. G. Magaña-Chavez and L. de los Santos Baños, *One-dimensional cellular automata with a unique active transition*, arXiv:2411.03601 (first public 2024-11-06), https://arxiv.org/html/2411.03601v3 .
2. P. P. B. de Oliveira, E. L. P. Ruivo, W. L. Costa, F. T. Miki and V. V. Trafaniuc, *Advances in the study of elementary cellular automata regular language complexity*, *Complexity* 21 (2016), 267–279, https://doi.org/10.1002/cplx.21686 .
3. E. L. P. Ruivo and P. P. B. de Oliveira, *Inferring the Limit Behavior of Some Elementary Cellular Automata*, *International Journal of Bifurcation and Chaos* 27 (2017), 1730028, https://doi.org/10.1142/S0218127417300282 .
4. L. Kassardjian, P. P. B. de Oliveira and E. Ruivo, *Extensions on the Analysis of Elementary Cellular Automata with Process Graphs*, *Advances in Cellular Automata*, 2025, https://doi.org/10.1007/978-3-031-78757-7_4 .
5. A. Ballier, *Limit sets of stable cellular automata*, arXiv:1301.3790, https://arxiv.org/abs/1301.3790 .
