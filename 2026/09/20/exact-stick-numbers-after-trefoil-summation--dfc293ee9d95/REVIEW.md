# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof uses three independently checkable established inputs: (i) for every nontrivial knot, \(b(K)<\operatorname{sb}(K)\le \operatorname{stick}(K)/2\), hence \(\operatorname{stick}(K)\ge2b(K)+2\); (ii) Schubert's formula \(b(K\#L)=b(K)+b(L)-1\); and (iii) the external-edge case in Sato's connected-sum construction, which gives \(\operatorname{stick}(K\#L)\le\operatorname{stick}(K)+\operatorname{stick}(L)-4\) when one summand has a minimum-stick representative with an external edge.

If both summands attain \(\operatorname{stick}=2b+2\), the bridge lower bound for their connected sum is exactly \(\operatorname{stick}(K)+\operatorname{stick}(L)-4\), so it matches Sato's geometric upper bound. Sato explicitly notes that both chiral trefoils have six-edge representations with external edges. Since a trefoil has bridge index \(2\), it satisfies the required equality and can be iterated. No assumption that the intermediate connected sum has an external edge is needed, because the newly attached trefoil supplies the external-edge factor at every step.

Cantarella--Rechnitzer--Schumacher--Shonkwiler prove that the nineteen listed knots have stick number \(10\) and bridge index \(4\), so each satisfies \(10=2\cdot4+2\). Substitution yields the exact family \(\operatorname{stick}=10+2m\).

## Originality

**PASS, to the best of our knowledge.**

The review separates the proposed contribution from its classical ingredients. Adams--Brennan--Greilsheimer--Woo (1997) already treat composition and determine exact stick numbers for compositions of a torus-knot family. Sato (2001) explicitly contains the external-edge four-stick saving and the square/granny trefoil examples. Schubert bridge additivity and the Kuiper--Jin bridge/superbridge bound are established results. None of those facts is claimed as new.

Searches were made under *stick number*, *polygon index*, *connected sum*, *composition*, *external edge*, *bridge index*, *superbridge index*, trefoil notation, the nineteen knot identifiers, and equivalent formulations of \(\operatorname{stick}=2b+2\). The 2025/2026 Cantarella et al. paper was checked directly: it proves the nineteen exact prime values and their \(4\)-bridge status, but contains no discussion of connected sums. No located source states the bridge-tight matching criterion or the resulting nineteen infinite families.

Residual originality risk remains material but limited: the argument is a short synthesis of classical inequalities, so an equivalent corollary may occur in older polygon-index/composition literature or as folklore under different terminology.

## Value

**PASS.**

Exact stick numbers are known for relatively few infinite families. The criterion explains when a geometric connected-sum construction is automatically optimal by matching it to a topological lower bound. Its immediate application converts nineteen recently determined isolated prime exact values into nineteen infinite families of exact composite stick numbers, with arbitrary chirality choices for the trefoil factors.

## Limitations

- The base knot must attain the universal lower bound \(\operatorname{stick}=2b+2\).
- The general two-factor criterion requires a minimum-stick external-edge representative of one summand.
- The nineteen base knots are not asserted to have minimum external-edge representatives.
- Only ordinary stick number is treated.
- Originality is to the best of our knowledge; equivalent folklore under *polygon index* remains possible.

## Sources checked

- Y. Sato, *The geometric shapes of polygonal knots* (2001), especially Theorem 2.2 and the external-edge case of its proof.  
  https://petit.lib.yamaguchi-u.ac.jp/6699
- C. C. Adams, B. M. Brennan, D. L. Greilsheimer, A. K. Woo, *Stick Numbers and Composition of Knots and Links* (1997).  
  https://doi.org/10.1142/S0218216597000121
- J. Schultens, *Additivity of bridge numbers of knots* (2003), giving a modern proof of Schubert's connected-sum formula.  
  https://doi.org/10.1017/S0305004103006832
- N. H. Kuiper, *A new knot invariant* (1987), and G. T. Jin, *Polygon indices and superbridge indices of torus knots and links* (1997), for the bridge/superbridge/stick relation.  
  https://doi.org/10.1007/BF01458070  
  https://doi.org/10.1142/S0218216597000170
- J. Cantarella, A. Rechnitzer, H. Schumacher, C. Shonkwiler, *New Upper Bounds for Stick Numbers* (2025/2026), Theorem 1 and its proof.  
  https://arxiv.org/abs/2508.18263  
  https://doi.org/10.1142/S0218216526500082
- KnotInfo, current stick-number table description.  
  https://knotinfo.org/descriptions/polygon_index.html
