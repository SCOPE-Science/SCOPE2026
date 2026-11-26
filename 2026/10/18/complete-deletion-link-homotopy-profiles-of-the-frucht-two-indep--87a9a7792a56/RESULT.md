# The twelve vertex-link homotopy types of the Frucht two-independence complex

## Finding

Let \(F\) be the labeled Frucht graph with edge set

```python
((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
 (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
```

Let \(K=\operatorname{Ind}_2(F)\), whose faces are subsets inducing only isolated vertices and single edges. The link of \(v\) is the complex on faces \(S\) disjoint from \(v\) for which \(S\cup\{v\}\in K\). Its geometric realization has the following unsuspended homotopy type:

| \(v\) | \(\operatorname{lk}_K(v)\) |
|:---:|:---|
| 0 | \(S^2\vee S^3\vee S^3\) |
| 1 | \(S^3\) |
| 2 | \(S^3\) |
| 3 | Contractible |
| 4 | \(S^3\) |
| 5 | \(S^3\) |
| 6 | \(S^2\vee S^3\) |
| 7 | \(S^3\vee S^3\) |
| 8 | \(S^2\vee S^3\) |
| 9 | \(S^2\vee S^3\vee S^3\) |
| 10 | \(S^3\) |
| 11 | \(S^3\vee S^3\vee S^3\) |

## Scope and motivation

The graph is simple and undirected, on vertices \(0,\ldots,11\). The link itself, rather than just its Betti numbers or its suspension, is the invariant here. In the deletion–link cofibration, the cofiber of the deletion inclusion gives the suspension of the link. It does not determine the unsuspended homotopy type without further information. In particular acyclicity by itself is not a proof that the link at vertex 3 is contractible.

## Proof and certificate

Enumerate all vertex subsets containing \(v\), retaining those for which every vertex in the subset has at most one neighbor in it. This criterion is equivalent to the defining component-size condition. Remove \(v\) from each retained subset to obtain the complete link face set. The program checks the correspondence of the listed graph with the Frucht LCF graph `[-5,-2,-4,2,5,-2,2,5,-2,-5,4,2]`.

In each nonempty-face poset, stage by vertex label in increasing order. At stage \(u\), pair each remaining face \(S\) omitting \(u\) with \(S\cup\{u\}\) if both are still unpaired. Construct the directed Hasse diagram with matched edges pointing up and all others pointing down, and topologically sort it. The complete sorts succeed for all twelve links. Discrete Morse theory therefore provides a CW model with the unpaired faces as cells, in their original dimensions. There is one critical zero-cell in every link, and no other dimensions except 2 and 3. The critical counts and the nonzero signed degree rows are as follows (zero columns may be inserted or omitted):

| \(v\) | Critical 2-cells | Critical 3-cells | Entries of the nonzero degree row, omitting zeros and disregarding order |
|:---:|:---:|:---:|:---|
| 0 | 1 | 2 | — |
| 1 | 0 | 1 | — |
| 2 | 1 | 2 | \(-1,1\) |
| 3 | 0 | 0 | — |
| 4 | 0 | 1 | — |
| 5 | 0 | 1 | — |
| 6 | 2 | 2 | \(-1,-1\) |
| 7 | 0 | 2 | — |
| 8 | 1 | 1 | — |
| 9 | 1 | 2 | — |
| 10 | 1 | 2 | \(1\) |
| 11 | 0 | 3 | — |

The checker computes these degree rows by signed gradient paths, using increasing label order on every simplex. For each critical 3-cell start with its ordinary oriented boundary. A critical 2-face is a terminal contributing its accumulated coefficient. When arriving at a matched lower face \(f\) with partner \(T\), propagate to each other boundary face \(g\) of \(T\), multiplying by \(-[\partial T:g]/[\partial T:f]\). A face matched downward cannot continue such a gradient path and contributes zero. Acyclicity makes this recursion finite. The sum of path weights is the integral Morse boundary, hence gives the degrees of the 3-cell attaching maps.

The 2-skeleton of the CW model is a wedge of 2-spheres; its \(\pi_2\) is free and the Hurewicz map identifies it with \(H_2\). Thus the degree homomorphism classifies all attaching maps from the wedge of source 2-spheres. Unimodular row and column changes are realized by homotopy equivalences of the corresponding wedges and leave the homotopy cofiber unchanged. Each displayed nonzero matrix has one nonzero row and a unit entry, so it becomes a single unit pivot and zero elsewhere. Its unit summand has contractible cofiber, while each remaining zero-attached 3-cell contributes a 3-sphere and each remaining 2-cell contributes a 2-sphere. This gives the table, including the model consisting of a single zero-cell at vertex 3.

## Verification

Run `python3 verify_link_wedges.py` with Python 3.9 or later. This standard-library program checks the full twelve-link enumeration, every matched Hasse diagram, and the signed degree patterns and wedge counts above. It ends with `ALL_12_FRUCHT_LINK_WEDGES_OK`.

## Relationship to prior work and limitations

*Integral vertex-deletion homotopy and inclusion profile of the Frucht two-independence complex* (record `e5c3e3ae1e81`) classifies the full complex, all deletions and the induced third-homology maps. In the deletion–link cofibration these determine link homology and the link suspension, not the unsuspended types established here by link-specific CW models. *The Frucht graph independence complex and its complete vertex-deletion classification* (record `8b7d9b2243c2`) concerns ordinary independence, which prohibits graph edges in faces, unlike two-independence. The graph families treated in the higher-independence work of Deshpande–Singh (arXiv:2001.05448) and Sawant's tree theorem (arXiv:2605.25150v1) do not supply the link calculation for this Frucht graph. This is a twelve-link classification for one graph; no general family theorem or priority certification is claimed.

The discrete Morse argument uses R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145.
