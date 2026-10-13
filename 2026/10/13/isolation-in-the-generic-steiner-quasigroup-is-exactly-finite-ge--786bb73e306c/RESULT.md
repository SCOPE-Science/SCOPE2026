# Isolation in the generic Steiner quasigroup is exactly finite generated closure

## Finding

Let \(T^*_{\mathrm{Sq}}\) be the complete model-completion theory of Steiner quasigroups in the language \(\{\cdot\}\). For every complete type \(p(\bar x)\in S_n(T^*_{\mathrm{Sq}})\) over the empty set and any realization \(\bar a\models p\),

\[
p\text{ is isolated}\quad\Longleftrightarrow\quad |\langle\bar a\rangle|<\infty.
\]

Barbina and Casanovas prove \(\operatorname{acl}(A)=\langle A\rangle\), so equivalently

\[
\boxed{\ p\text{ is isolated}\iff |\operatorname{acl}(\bar a)|<\infty.\ }
\]

As a sharp arity consequence, every complete \(1\)- and \(2\)-type is isolated, whereas for every \(n\ge3\) there are exactly \(2^{\aleph_0}\) nonisolated \(n\)-types. Thus arity \(3\) is the first arity at which nonisolated types occur.

## Assumptions and scope

The theory is the pure Steiner-quasigroup theory studied by Silvia Barbina and Enrique Casanovas, not an arbitrary expansion or another Steiner-system theory. Types are complete types over \(\varnothing\). A Steiner quasigroup satisfies
\[
x\cdot x=x,\qquad x\cdot y=y\cdot x,\qquad x\cdot(x\cdot y)=y.
\]
The result uses the authors' quantifier elimination, the local finiteness and primeness of the Fraïssé limit \(M_F\), their continuum family of three-generated types, and their characterization \(\operatorname{acl}(A)=\langle A\rangle\).

## Proof

Suppose first that \(\langle\bar a\rangle\) is finite. Every finite Steiner quasigroup embeds into the Fraïssé limit \(M_F\); let \(\bar b\in M_F\) be the image of \(\bar a\) under such an embedding of generated substructures. The tuples \(\bar a\) and \(\bar b\) have the same quantifier-free type, because every term equality is read inside the isomorphic generated subquasigroups. Quantifier elimination therefore gives \(\operatorname{tp}(\bar a)=\operatorname{tp}(\bar b)\). Proposition 4.4 of Barbina--Casanovas proves that every tuple from \(M_F\) has isolated type. Hence \(\operatorname{tp}(\bar a)\) is isolated.

Conversely, let \(p=\operatorname{tp}(\bar a)\) be isolated by a formula \(\varphi(\bar x)\). Since \(p\) is consistent and \(T^*_{\mathrm{Sq}}\) is complete, \(T^*_{\mathrm{Sq}}\models\exists\bar x\,\varphi(\bar x)\). In particular the prime model \(M_F\) contains a tuple \(\bar b\) satisfying \(\varphi\), and therefore \(\bar b\models p\). Equal complete types imply the same equalities between all terms, so the assignment
\[
t(\bar a)\longmapsto t(\bar b)
\]
is a well-defined isomorphism \(\langle\bar a\rangle\cong\langle\bar b\rangle\). The Fraïssé limit is locally finite, hence \(\langle\bar b\rangle\), and therefore \(\langle\bar a\rangle\), is finite. Corollary 5.5 then identifies this generated substructure with algebraic closure.

For one variable, the generated subquasigroup is a singleton. Two equal elements again generate one point, while two distinct elements \(a,b\) generate exactly \(\{a,b,a\cdot b\}\). Thus all \(1\)- and \(2\)-types are isolated.

Barbina--Casanovas Theorem 3.3 constructs \(2^{\aleph_0}\) distinct complete \(3\)-types whose realizations generate countably infinite Steiner quasigroups. By the equivalence above, every one of those types is nonisolated. Repeating coordinates carries these types injectively into every higher arity while preserving the same infinite generated closure. A countable language has at most \(2^{\aleph_0}\) complete \(n\)-types, so the number of nonisolated \(n\)-types is exactly \(2^{\aleph_0}\) for every \(n\ge3\).

## Verification

The bundled verifier checks the finite algebraic facts used at low arity. It exhausts all \(3^9=19{,}683\) binary operations on three labeled points and finds exactly one Steiner-quasigroup table, verifies one-generator and two-generator closure sizes, and independently checks the seven-point Fano Steiner quasigroup, including that two generators close to at most three points while three independent points generate all seven. It returns:

`VERIFY_OK 165 exact assertions`

The isolation equivalence itself is a theorem-level deduction from the cited model-theoretic results; finite computation is not presented as a proof of that infinite statement.

## Relationship to prior work

Barbina and Casanovas prove separately that \(M_F\) is prime and locally finite (Proposition 4.4 and the preceding Fraïssé-limit discussion), that \(T^*_{\mathrm{Sq}}\) eliminates quantifiers, that \(\operatorname{acl}(A)=\langle A\rangle\) (Corollary 5.5), and that there are continuum many complete three-variable types arising from three-generated countable Steiner quasigroups (Theorem 3.3). The inspected paper does not state the biconditional “isolated type iff finite generated closure/algebraic closure,” nor the resulting exact nonisolated-type spectrum.

A previously recorded result for the same theory determines the total empty-set type cardinalities \(1,1,2,2^{\aleph_0},\ldots\). That result does not distinguish isolated from nonisolated types. The present statement adds a structural criterion for isolation and identifies the entire nonisolated locus by arity.

Targeted published-finding corpus searches for isolated types in generic Steiner quasigroups, exact web searches under equivalent finite-closure formulations, direct full-text inspection of the source, and searches of the current and preceding cumulative ledgers found no equivalent statement. The main residual priority risk is an unindexed folklore observation obtainable by combining standard prime-model facts with the paper's local-finiteness and closure results.

## Limitations

The theorem concerns types over the empty set. It does not classify isolated types over arbitrary parameter sets, describe the topology or Borel complexity inside the continuum nonisolated locus, or enumerate the isolated \(n\)-types for \(n\ge3\). The deduction is short once the source's results are assembled, so independent priority remains uncertain. No independent audit has been performed.

## References

1. Silvia Barbina and Enrique Casanovas, “Model theory of Steiner triple systems,” arXiv:1805.06767; *Journal of Mathematical Logic* 20 (2020), 2050010, DOI 10.1142/S0219061320500105. First arXiv submission: 17 May 2018.
2. The same article, Theorem 3.3, Proposition 4.4, and Corollary 5.5.
