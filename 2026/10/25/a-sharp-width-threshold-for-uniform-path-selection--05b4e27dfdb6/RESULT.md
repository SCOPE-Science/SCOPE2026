# A sharp width threshold for uniform path selection

## Finding

Let \(T_e\subseteq 2^{<\omega}\) be a computably enumerable, prefix-closed binary tree, and write \([T_e]\) for its infinite paths. Under the promise \([T_e]=\{X_e\}\), width at most one admits a uniform exact path selector, whereas width at most two admits no uniform single-program selector even up to finitely many errors: no total computable \(A(e,n)\in\{0,1\}\) satisfies \(\exists N\,\forall n\ge N,\ A(e,n)=X_e(n)\) for every index \(e\) of a width-at-most-two tree with exactly one path.

## Assumptions and scope

A binary tree is a prefix-closed set of finite binary strings. Its width is \(w(T)=\sup_n |T\cap 2^n|\). An index enumerates the tree computably enumerable (c.e.); membership need not be decidable. The promise \([T_e]=\{X_e\}\) says there is exactly one infinite path. A uniform finite-error selector is one total computable function of the index and coordinate whose output differs from that path at only finitely many coordinates. The width bound and the singleton-path promise are promises on the input class, not procedures for recognizing that class.

## Proof

First suppose \(w(T_e)\le1\) and \([T_e]\ne\varnothing\). Every level has exactly one string: the path supplies one at each length, and width one excludes a second. On input \(n\), wait for the c.e. enumeration to produce the unique string of length \(n+1\). Output its last bit. This halts for every \(n\) under the nonempty-path promise and returns the path exactly. The procedure is uniform in the tree index.

For the width-two obstruction, suppose a total computable candidate \(A(e,n)\in\{0,1\}\) eventually agrees with the unique path of every c.e. binary tree of width at most two having exactly one path. Use the recursion theorem to obtain an index \(e\) for the following c.e. tree construction, which can refer to its own index. Enumerate the empty string initially and enumerate every prefix whenever a node is added. Maintain one current finite spine. At stage \(s\), extend that spine to a fresh level \(n_s\) above every node enumerated so far, and enumerate both one-bit extensions at coordinate \(n_s\). While waiting for \(A(e,n_s)\), extend the zero child provisionally, one level at a time. If the computation never returns, this provisional branch continues forever and the sibling remains finite, so the tree still has exactly one path. Hence, under the assumed totality of \(A\) on the promised class, the computation must return some bit \(b\).

If \(b=1\), keep extending the zero child; if \(b=0\), stop extending the provisional zero child and extend the one child past the greatest level reached by the provisional branch. In either case the surviving path has bit \(1-b\) at coordinate \(n_s\). Choose the next fresh level above all nodes then enumerated. Every abandoned side branch is finite and lies below the next split, so at each level there are at most two nodes. Each stage leaves one branch to continue; if a stage stalls, the provisional zero branch is the unique infinite path. Thus the constructed tree is always c.e., prefix-closed, of width at most two, and has exactly one infinite path.

Under the assumed totality, all stages finish and produce infinitely many increasing coordinates \(n_s\) with \(X_e(n_s)=1-A(e,n_s)\). Therefore \(A(e,\cdot)\) disagrees with the unique path at infinitely many coordinates, contradicting eventual agreement. No such uniform finite-error selector exists for the width-at-most-two singleton-path class. The obstruction is about uniformity from an index, not the individual computability of the unique path.

## Verification

The width-one algorithm is total because every level's unique string is eventually enumerated. The diagonal construction uses the recursion theorem only to obtain a self-referential enumerator; it does not assume that tree membership is decidable. The width bound follows from allowing at most one active split and starting the next split above all previously enumerated nodes. The path-uniqueness promise holds both if a simulated selector computation stalls (the provisional branch continues) and if it returns (one child is continued and the other becomes finite). No finite experiment is used to infer the infinite conclusion.

## Relationship to prior work

Kaufmann and Kummer's work on quantitative uniformity establishes a broad nonuniformity phenomenon for branches of c.e. bounded-width trees and gives an optimal list size of \(2n-1\) programs for trees of width at most \(n\), where one listed program must approximate a branch up to finitely many errors. The accessible abstract does not specify whether the lower-bound construction remains within the subclass of trees having exactly one path. The result here isolates that singleton-path restriction and contrasts width one, where exact uniform selection is possible, with width two, where even a single finite-error selector is impossible. The full text of the broad prior result was not available for a complete restriction-by-restriction comparison, so novelty is limited to this precise formulation and remains subject to that stated risk. Binns and Kjos-Hanssen study reverse-mathematical principles for paths through infinite binary trees with restricted branching; their stated results concern path existence and subsystem strength, not this index-uniform finite-error selection question.

## Limitations

The theorem does not determine the least number of programs needed for a finite list on the singleton-path subclass. It does not give a uniform index for the unique path, and it makes no claim about trees whose width is unbounded, trees over larger branching alphabets, or promises that cannot be assumed as input conditions. The comparison with Kaufmann–Kummer is limited to accessible abstract and bibliographic material; an uninspected proof could already contain the singleton-path restriction.

## References

1. S. Kaufmann and M. Kummer, “On a Quantitative Notion of Uniformity,” *Fundamenta Informaticae* 25(1), 59–78 (1996), DOI: 10.3233/FI-1996-25106. The conference version is in *Mathematical Foundations of Computer Science 1995*, LNCS 969, pp. 169–178, DOI: 10.1007/3-540-60246-1_123.
2. S. Binns and B. Kjos-Hanssen, “Finding paths through narrow and wide trees,” arXiv:1408.2857 (first posted 2014-08-12), https://arxiv.org/abs/1408.2857.
