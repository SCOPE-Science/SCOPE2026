# Review of the sharp rarefaction detection theorem

## Correctness — PASS

For every noncaterpillar unrooted binary tree and \(n\ge7\), at most four leaves can individually destroy every triply internal node upon deletion. Equality entails two two-leaf branches at a unique triply internal vertex and a rooted comb for the third branch. Sequentially uniform leaf deletion then gives exactly \((k)_4/(n)_4\), attained uniquely by that shape for \(k<n\). The six-leaf branch-product census is independently derived without treating finite checks as the proof. The standalone verifier enumerates every unlabelled shape through eleven leaves and directly rebuilds sampled subtrees for an independent check. Critical boundary cases \(k=6\), \(k=n\), and \(n=6\) are explicitly separated.

## Originality — PASS, with residual risk

The closest inspected papers treat unrooted split-size objectives (Fischer–Liebscher 2015), rooted fixed-shape maximal inducibility (Czabarka–Székely–Wagner 2016; Czabarka et al. 2018), and the number of distinct rooted leaf-induced shapes (Dossou-Olory–Boadi 2022). Their stated quantities do not imply the sharp unrooted finite lower bound, the all-sample-size equality characterization, or its pruning mechanism. Targeted literature and published research-record searches found no dominating statement. General leaf-induced-profile literature may contain an equivalent formulation not captured by the searches; independent bibliographic verification remains unperformed.

## Value — PASS

The result is a sharp non-asymptotic power floor for a natural topology-only phylogenetic rarefaction diagnostic, with a unique worst-case shape and an explicit fourth-power sampling cost for six-taxon tests. It quantifies a genuine limitation of repeated small-taxon studies rather than merely certifying that some noncaterpillar sample exists. The exact finite cutoff at six leaves and simultaneous all-\(k\) extremizer are natural components of the same mathematical claim.

Self-review: passed. Independent audit: not yet performed.
