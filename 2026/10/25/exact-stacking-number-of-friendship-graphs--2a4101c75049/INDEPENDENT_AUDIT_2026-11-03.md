# Independent mathematical audit

## correctness

PASS

The final repaired claim is stack(F_k)=4k for every integer k>=1, with every size-4k configuration reaching the hub. From outer counts (a_i,b_i), direct-to-hub preprocessing leaves S<=2r odd residues and H=(4k+c(h)-S)/2>=2k-r>=r; if H>=r+1 one hub-assisted elimination per residual pair consumes one hub pebble. Equality forces all 2k leaves initially odd and some pair a>=3,b>=1; two internal transfers make that pair even without changing its direct-to-hub contribution, decreasing residual pairs from k to k-1. For the lower witness (2k+1,0) plus k-1 pairs (1,1), the mass ledger gives 2delta0+3A+C<=2k+1, delta0<=k and light activated delta_i<=-1. The SOURCE proof makes an invalid inference 3A+C<=1 ==> C=0; repaired RESULT.md proves C=1 impossible because A=0, B=k, one internal transfer gives both coordinates odd while total mass equation forces zero. Thus equality delta0=k implies the heavy pair retains a frozen singleton. At the last light-pair activation q=k-2 and hub>=2 forces equality, after which hub<=1 permanently; the final light pair cannot vanish without a new frozen hub pebble. k=1 triangle and threshold monotonicity for t>2k+1 finish the universal claim. Independent exact reachability from separately written exhaustive Python script checked all canonical size-4k configurations for k=1..4 (9,92,759,5265) reach hub and all stated size-(4k-1) witnesses are nonstackable. That finite work corroborates, but the analytical proof covers all k.

## originality

PASS

Best-knowledge: the 2026 undirected stacking/clearing primary paper introduces exactly this invariant and proves the general 3alpha+1 bound, K_n, complete bipartite/multipartite and path formulas, but not F_k for k>=2; the 2026 directed follow-up gives the directed-cycle value and general existence theorem, without a bidirected friendship family computation. The 2026 ASH sequel addresses conditional cycle/tree and perfect-clearability results, rather than the all-k friendship formula (only abstract accessible for this source). Exact published small-graph report was inspected as source .tex: its selected table includes K3 but no k>=2 friendship graph. Semantic Resultary searches found friendship graphs for zero forcing, edge resolvers, dissociation and windmill general-position polynomials, not stacking. Originality is limited to the k>=2 exact threshold and stronger hub-only statement, not k=1 or the invariant. Priority risk remains.

## value

PASS

This is a motivated sharp exact classification for the just-introduced stacking invariant on the standard infinite block-graph family F_k, beyond K3 and complete multipartite families. The 4k threshold exceeds the general 3k+1 independence bound by k-1 for every k>=2. The sharp obstruction and hub-assist parity/debt mechanism are mathematical structural contributions that could be used for more general graph bouquets. Not merely a finite table or known-parameter substitution; no extension to larger windmill blocks, clearing, or ASH is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
