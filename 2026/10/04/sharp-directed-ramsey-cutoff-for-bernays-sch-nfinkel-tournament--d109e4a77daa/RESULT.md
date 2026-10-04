# Sharp directed-Ramsey cutoff for Bernays–Schönfinkel tournament spectra
## Finding
Let \(R_{\to}(\ell)\) denote the directed Ramsey number: the least integer \(r\) such that every tournament on \(r\) vertices contains a transitive subtournament on \(\ell\) vertices. Fix \(k\ge 0\) and \(\ell\ge 2\). Consider finite-tournament sentences in Bernays–Schönfinkel form
\[
\exists x_1\cdots\exists x_k\,\forall y_1\cdots\forall y_\ell\,\psi,
\]
where \(\psi\) is quantifier-free. The tournament axioms can be included in the same prefix because \(\ell\ge2\).

The sharp finite-spectrum cutoff is
\[
N_T(k,\ell)=k+\bigl(R_{\to}(\ell)-1\bigr)2^k.
\]
If such a sentence has a model with more than \(N_T(k,\ell)\) vertices, then it has a model of every order \(n\ge k+\ell\). Hence, if its spectrum is finite, its maximum is at most \(N_T(k,\ell)\). For every \(k,\ell\), this endpoint is attained by a sentence in the same prefix class.

For example, \(R_{\to}(3)=4\), so the three-universal tournament ceiling is \(k+3\cdot2^k\). The classical small directed-Ramsey values also give \(R_{\to}(4)=8\), \(R_{\to}(5)=14\), and \(R_{\to}(6)=28\).

## Assumptions and scope
The vocabulary has equality and one binary relation \(E\), interpreted as the arc relation of a finite tournament: \(E(u,u)\) never holds and, for distinct \(u,v\), exactly one of \(E(u,v)\) and \(E(v,u)\) holds. The theorem concerns exactly \(k\) leading existential variables and \(\ell\) universal variables, with arbitrary quantifier-free Boolean combinations in the matrix. Existential witnesses need not be distinct unless the sentence itself requires that.

The spectrum is the set of finite model orders. The sharpness construction below conjoins pairwise distinctness of the witnesses, so all \(2^k\) witness-orientation profiles are available. No claim is made about which subsets below the ceiling can occur.

## Proof
Let \(G\models\Phi\), and choose a witnessing tuple \((a_1,\ldots,a_k)\). Let \(U\) be the set of distinct witness values and write \(s=|U|\le k\). Every vertex \(v\notin U\) has an orientation profile toward \(U\): for each \(u\in U\), record whether \(E(v,u)\) or \(E(u,v)\) holds. There are at most \(2^s\le2^k\) such profiles.

Assume
\[
|G|>k+\bigl(R_{\to}(\ell)-1\bigr)2^k.
\]
Then \(|G\setminus U|>(R_{\to}(\ell)-1)2^k\). By pigeonhole, one profile class contains at least \(R_{\to}(\ell)\) vertices. By the definition of the directed Ramsey number, that class contains a transitive subtournament \(X\) of order \(\ell\).

Pass to the induced subtournament \(G[U\cup X]\). It still satisfies \(\Phi\): the chosen existential witnesses remain, and a universal quantifier-free condition is preserved when the domain is restricted to an induced substructure containing those witnesses.

Now replace \(X\) by an arbitrarily large transitive tournament \(Z\), orienting every arc between \(Z\) and each witness \(u\in U\) exactly as the common profile of \(X\) prescribes. Keep the tournament on \(U\) unchanged. Call the resulting tournament \(H\).

To check \(H\models\Phi\), take any assignment to \(y_1,\ldots,y_\ell\). Fix every value lying in \(U\). Among the values lying in \(Z\), there are at most \(\ell\) distinct vertices. Because both \(Z\) and \(X\) are transitive, those distinct vertices admit an order-preserving injection into \(X\). Apply that injection and preserve repeated values. The resulting \(\ell\)-tuple in \(G[U\cup X]\) has exactly the same equality pattern, the same arcs among universal values, and the same arcs between universal values and all existential witnesses. Thus every atomic formula occurring in \(\psi\) has the same truth value on the two assignments. Since \(G[U\cup X]\models\Phi\), the matrix holds in \(H\).

Choosing \(|Z|=n-s\) gives a model of every order \(n\ge k+\ell\), because \(n-s\ge\ell\). This proves the cutoff.

For sharpness, fix a tournament \(Q\) on \(R_{\to}(\ell)-1\) vertices with no transitive \(\ell\)-vertex subtournament. Such a \(Q\) exists by minimality of \(R_{\to}(\ell)\). Construct a sentence that:

1. requires the \(k\) witnesses to be pairwise distinct;
2. requires the whole structure to be a tournament; and
3. says that whenever \(y_1,\ldots,y_\ell\) are distinct non-witness vertices having the same orientation profile toward all witnesses, their induced tournament is not transitive.

All three conditions fit the required prefix. The third is quantifier-free because transitivity of a labeled \(\ell\)-vertex tournament is the finite disjunction, over all \(\ell!\) linear orders, that every pair is oriented forward in that order.

Every witness-profile class therefore has size at most \(R_{\to}(\ell)-1\), so every model has at most \(N_T(k,\ell)\) vertices. Conversely, realize every one of the \(2^k\) profiles by a disjoint copy of \(Q\), orient arcs between distinct profile classes arbitrarily, and orient each copy toward the witnesses according to its profile. This is a tournament of exactly
\[
k+\bigl(R_{\to}(\ell)-1\bigr)2^k
\]
vertices satisfying the sentence. Hence the endpoint is optimal.

## Verification
The proof is symbolic. The attached checker exhaustively enumerates all \(2^6=64\) labeled tournaments on four vertices, confirms that each contains a transitive triple, verifies that a directed 3-cycle avoids a transitive triple, and checks the specializations \(N_T(k,3)=k+3\cdot2^k\) for \(0\le k\le8\). It also verifies the size-seven sharp construction for \((k,\ell)=(1,3)\).

## Relationship to prior work
The 2010 survey by Pikhurko and Verbitsky gives the graph Bernays–Schönfinkel finite/cofinite spectrum argument: equal witness-neighborhood profiles plus an undirected Ramsey-homogeneous \(\ell\)-set yield a clonable block. The exact graph endpoint recorded in the present ledger replaces the survey's coarse \(2^k4^\ell\) bound by the sharp ordinary Ramsey number.

Tournament Ramsey theory asks for the least order forcing a transitive subtournament. Sánchez-Flores's 1994 paper treats this invariant and its small exact values, building on the Erdős–Moser problem. Combining that tournament invariant with the Bernays–Schönfinkel profile/cloning mechanism yields the exact tournament endpoint above. Targeted published-finding corpus, web, and ledger searches did not locate this fixed-prefix sharp spectrum formula or an equivalent implication statement.

The closest general first-order result located is the fixed-vocabulary Bernays–Schönfinkel Ramsey theorem of Pikhurko, Spencer, and Verbitsky, which gives an eventual-model bound without this tournament-specific optimal constant. The closest quantitative spectrum theorem is the graph case in the Pikhurko–Verbitsky survey.

## Limitations
The theorem is specific to tournaments and to the \(\exists^k\forall^\ell\) prefix. Exact numerical evaluation inherits the difficulty of directed Ramsey numbers: values are known only for small \(\ell\), and even \(R_{\to}(7)\) is not currently exact. The theorem determines the largest possible finite-spectrum endpoint, not the full collection of spectra below it. The originality check cannot exclude an unindexed folklore observation, especially because the proof is a short synthesis of two classical Ramsey mechanisms.

## References
- Adolfo Sánchez-Flores, “On Tournaments and Their Largest Transitive Subtournaments,” *Graphs and Combinatorics* 10 (1994), 367–376. DOI: 10.1007/BF02986687.
- Oleg Pikhurko and Oleg Verbitsky, “Logical complexity of graphs: a survey,” arXiv:1003.4865 (2010), especially the Bernays–Schönfinkel spectrum argument in Section 7.3.
- Oleg Pikhurko, Joel Spencer, and Oleg Verbitsky, “Succinct definitions in the first order theory of graphs,” *Annals of Pure and Applied Logic* 139 (2006), 74–109. DOI: 10.1016/j.apal.2005.04.003.
- Paul Erdős and Leo Moser, “On the representation of directed graphs as unions of orderings,” *Publ. Math. Inst. Hung. Acad. Sci.* 9 (1964), 125–132.
