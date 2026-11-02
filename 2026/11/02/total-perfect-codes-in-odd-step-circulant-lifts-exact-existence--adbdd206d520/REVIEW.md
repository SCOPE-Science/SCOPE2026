# Scientific review: odd-step circulant total perfect codes

## Correctness (C): PASS

The claim concerns all integers \(r\ge2\) and \(n\ge4r\). The open-neighborhood equations contain exactly \(2r\) terms, with no repeated neighbor indices. Subtracting equations at positions two apart cancels every interior term and forces period \(4r\) for any solution, with no binary or positivity assumption needed for that cancellation. Counting open neighborhoods gives \(2r\mid n\); the forced shorter period when \(4r\nmid n\) produces an even number of selected neighbors, contradicting one. When \(4r\mid n\), the neighborhood offsets cover every opposite-parity residue exactly once. One chosen residue in each parity is therefore necessary and sufficient. Exactly \((2r)^2\) labelled choices result. The standalone checker confirms 6 direct subset censuses, 45 independent seed-recurrence censuses, and 7,800 constructed-code tests. The infinite theorem rests on the written argument, not on bounded computations.

## Originality (O): PASS, with identified historical risks

The closest directly relevant primary paper, Cameron–Yap–Zhou, arXiv:2507.11871, Theorem 5.3, classifies the base order \(n=4r=2|S|\) but does not state the classification for arbitrary multiples of \(4r\). Other results in its Section 5 impose subgroup or coprimality conditions that do not subsume the non-subgroup codes at these larger orders. Koohestani–Mojdeh–Ghasemi, arXiv:2510.20376, also covers the base-order case via Cayley sum graphs; the odd-step bipartite graphs here are isomorphic to those Cayley sum graphs under negation on one parity class. That equivalence was specifically considered, and the paper's relevant later results also do not imply all-lift uniqueness. The new contribution is that **all** total perfect codes on **every** cyclic lift are pulled back from the base, with the same exact count, and no additional patterns occur. The main published existence criteria and ordinary efficient-domination classifications were not treated as new. Searches of previous records, equivalent aliases, and published mathematical literature found no stronger covering claim. A 2007 closed-neighborhood paper could not be read in full, and an equivalent result under a different tiling terminology remains possible. These specific uncertainties do not supply a known implication covering the all-lift theorem. No independent priority certification is claimed.

## Mathematical value (V): PASS

The open-neighborhood analogue of perfect codes is the central object of both motivating recent papers. The present two-parameter family of connected regular circulants admits a complete all-orders classification of both existence and the exact number of codes. The key structural conclusion is **rigidity under every cyclic lift**: a code satisfying local constraints is forced to have bounded period independent of the ambient order. The count and explicit list are exact and stable across arbitrarily large lifts; this is a natural complete classification, not a selected finite parameter or an unmotivated numerical table. The two-step cancellation also gives a reusable method for sliding open-neighborhood constraints.

## Closest literature and limitations

- P. J. Cameron, R. S. Yap and S. Zhou, *Perfect codes in Cayley graphs of abelian groups*, arXiv:2507.11871, especially Section 5 and Theorem 5.3. Base order covered, all cyclic lifts not stated.
- M. Koohestani, D. A. Mojdeh and M. Ghasemi, *Total perfect codes in Cayley sum graphs of cyclic groups*, arXiv:2510.20376, especially Theorems 3.4, 3.7 and 3.13. Cayley sum equivalence checked; base order covered, all-lift classification not stated.
- R. Feng, H. Huang and S. Zhou, *Perfect codes in circulant graphs*, arXiv:1703.08652. General existence methods and different ordinary perfect-code results; no covering all-lift total-code census found.
- N. Obradović, J. Peters and G. Ružić, *Efficient domination in circulant graphs with two chord lengths*, DOI:10.1016/j.ipl.2007.02.004. Abstract accessible, full text not accessed; it studies ordinary (closed) efficient domination, not the open variant.

The claim is restricted to the symmetric consecutive odd-step interval and does not classify arbitrary generating sets. Historical priority remains provisional. Self-review has been completed; independent mathematical review has not yet occurred.

Self-review: passed. Independent audit: not yet performed.
