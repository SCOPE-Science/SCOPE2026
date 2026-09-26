# Independent audit — 2026/09/09/066

## Correctness — PASS

The 15 listed edges on 13 vertices give cycle rank 15−13+1=3. For induced matchings, deletion of the common vertex leaves three disjoint P4 paths, each with induced matching number one, giving at most three if the matching avoids 0. If it uses an edge incident to 0, it cannot use another edge from that lobe and can take at most one from each other lobe. The displayed three-edge witness therefore proves im=3.

I found an independent topological proof of regularity, avoiding the supplied rational boundary matrices. In the independence complex Δ=Ind(G), deletion of 0 is the join of three Ind(P4), each a contractible three-edge path, so Δ−0 is contractible. The link of 0 is the join of three Ind(P2)=S⁰, hence S². Since Δ is the union of the contractible deletion and the cone on its link, its reduced homology has one Q class in degree 3 (indeed Δ is homotopy equivalent to S³). Hochster gives reg(S/I)≥4. The vertex-deletion inequality gives reg(G)≤max(reg(three P4),1+reg(three P2))=max(3,4)=4, using the standard forest/induced-matching equality for these paths. Thus reg=4 and the gap is one. This independently reproduces the material result without the machine logs.

## Originality — PASS, narrow counterexample

The checked unicyclic and bicyclic papers treat at most two cycles and do not supply this tricyclic wedge obstruction. The elementary topology here makes the specific example transparent; it is a local counterexample to the proposed universal wedge equality, not a tricyclic classification.

## Scientific value — PASS, limited

The example rules out the stated all-wedges equality and identifies a concrete obstruction any tricyclic classification must accommodate. It does not address attached trees, minimality, or characteristic dependence in the record's computation; the topological argument actually gives the lower homology over any field.

## Sources

- Original RESULT.md and METADATA.json; independent independence-complex decomposition and induced-matching argument above.
- Alilooee–Kara–Selvaraja, https://arxiv.org/abs/1702.00916 .
- Cid-Ruiz et al., https://arxiv.org/abs/1802.07202 .
