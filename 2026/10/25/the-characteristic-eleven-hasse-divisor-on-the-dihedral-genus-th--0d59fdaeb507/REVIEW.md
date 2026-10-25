# Self-review

## Correctness — PASS
For the smooth family \(y^2=x^8+a x^4+1\) in characteristic \(11\), binomial coefficient extraction yields the sparse Hasse--Witt matrix with nonzero positions \((1,3),(2,2),(3,1)\). The exact factors \(u=5-a^2\) and \(v=a(a^2-3)(a^2+1)\) are coprime and squarefree, so their zero sets give all stable Frobenius ranks and determinant vanishing orders. The proof explicitly handles smoothness \(a^2\ne4\), semilinear iteration and the Cartier-operator relation. `verify_p11.py` independently checks the polynomial identities and separability of factors. The finite-field sample is corroborative only.

## Originality — PASS (qualified)
Gutierrez--Shaska give the same natural family and moduli parameter \(w=a^2\). Harvey--Sutherland supply the general Hasse--Witt coefficient formula. Paulhus gives genus-three Jacobian decomposition context; Achter--Pries give generic hyperelliptic p-rank stratum dimensions. Their inspected relevant sections do not tabulate the seven characteristic-eleven geometric exceptional parameters or distinguish the double and simple Hasse divisor intersections. Literature searches for equivalent families, alternate parameters and rank strata revealed no stronger covering result. Other modular descriptions of this exact divisor remain possible; missing indexed results alone do not establish novelty.

## Mathematical value — PASS
The explicit length-nine nonordinary divisor (two double plus five simple points) along the intrinsic dihedral pencil describes a nontransverse modular incidence and determines every geometric p-rank and a-number in this automorphism-symmetric genus-three family. This is more than a field-element enumeration: the scheme-theoretic multiplicities are established uniformly over the algebraic closure. It is a natural complete family classification; it does not imply a general theorem for all genus-three curves.

## Limitations
There is no classification of Newton polygons beyond p-rank, and no assertion about compactification of the pencil. Equivalent historical treatment remains a residual risk. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
