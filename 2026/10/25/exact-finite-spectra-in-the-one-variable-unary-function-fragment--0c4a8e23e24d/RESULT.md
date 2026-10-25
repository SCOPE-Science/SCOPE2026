# Exact finite spectra in the one-variable unary-function fragment

## Finding

For sentences in the one-variable-symbol fragment \(\mathrm{FO}^{1}\) over the signature consisting only of one unary function \(f\) and equality, with nonempty finite models, the set of model sizes is exactly a finite union of tails \(T_N=\{n\in\mathbb N_{>0}:n\ge N\}\) and shifted cycle-length semigroups \(S_L=s(L)+\langle L\rangle\), where \(N\ge1\), \(L\subseteq\mathbb N_{>0}\) is finite and nonempty, \(s(L)=\sum_{\ell\in L}\ell\), and \(\langle L\rangle=\{\sum_{\ell\in L}k_\ell\ell:k_\ell\in\mathbb N_0\}\). The empty spectrum is also allowed.

Here \(\mathrm{FO}^{1}\) means one variable symbol that may be rebound, not one universal quantifier. A shifted semigroup \(S_L\) consists of the sizes of disjoint unions of cycles in which every length in \(L\) occurs at least once and no other cycle length occurs.

## Assumptions and scope

Structures are finite and nonempty; the vocabulary is exactly equality and one total unary function \(f\), with no constants or additional relation/function symbols. The spectrum of a sentence is the set of positive integers that occur as sizes of its finite models. Terms have the form \(f^i(x)\). The statement concerns the one-variable-symbol fragment, not fragments bounded by the number of universal quantifiers.

## Proof

Fix a sentence \(\varphi\), and let \(d\) be the maximum iterate depth in any term occurring in it. Every formula using only the variable symbol \(x\) is equivalent to a Boolean combination of quantifier-free formulas in \(x\) and closed formulas of the form \(\exists x\,\theta(x)\), with \(\theta\) quantifier-free. This follows by structural induction: at a quantifier, put the Boolean combination into disjunctive normal form; each closed conjunct can be pulled outside the quantifier, leaving an existential closure of a quantifier-free conjunct. Nonempty domains make existential quantification of a closed conjunct equivalent to that conjunct. Thus the truth of \(\varphi\) depends only on which quantifier-free orbit types are realized.

For the finite list of terms \(x,f(x),\ldots,f^d(x)\), a point has one of the following types:

* \( (t,\ell) \), where \(t\ge0\), \(\ell\ge1\), and \(t+\ell\le d\), if the first repeated iterate is \(f^{t+\ell}(x)=f^t(x)\). The orbit has preperiod \(t\) and eventual cycle length \(\ell\).
* \(\star\), if these first \(d+1\) iterates are pairwise distinct.

These types determine every equality between the terms, so they determine every quantifier-free formula in \(x\). Consequently the spectrum of \(\varphi\) is a finite union of the size sets associated with the realized-type sets \(R\) on which \(\varphi\) is true.

Consider any realized-type set \(R\) that has at least one finite model. If \(R\) contains \(\star\), take a point of that type and add a new leaf \(y\) with \(f(y)=z\), where \(z\) lies on the eventual cycle of that point. The new point's type is already in \(R\): it is \(\star\) when the cycle is too long for a repeat within depth \(d\), and otherwise it is the already-realized type \( (1,\ell) \). Existing forward orbits do not change. Hence one may add any number of leaves without changing \(R\), so the sizes realizing \(R\) form a tail.

If \(R\) has a type \( (t,\ell) \) with \(t\ge1\), then it also realizes \( (1,\ell) \). Adding a leaf directly to that cycle realizes no new type, and again every larger size is possible. Thus this case also gives a tail.

The remaining case has neither \(\star\) nor any type with \(t\ge1\). Every element must then lie on a cycle of length at most \(d\): a nonperiodic point would realize either a positive-preperiod type or \(\star\), and a longer cycle would realize \(\star\). Let \(L\) be the nonempty set of cycle lengths actually present. Every \(\ell\in L\) must occur at least once, and all components are cycles with lengths in \(L\). The possible sizes are exactly

\[ S_L=\sum_{\ell\in L}\ell+\left\{\sum_{\ell\in L}k_\ell\ell:k_\ell\in\mathbb N_0\right\}. \]

This proves that every spectrum is a finite union of the stated sets, together possibly with the empty set.

For the converse, given a finite nonempty \(L\), let \(\operatorname{Per}_\ell(x)\) assert \(f^\ell(x)=x\) and \(f^j(x)\ne x\) for every \(1\le j<\ell\). The one-variable sentence

\[ \forall x\,\bigvee_{\ell\in L}\operatorname{Per}_\ell(x)\quad\land\quad\bigwedge_{\ell\in L}\exists x\,\operatorname{Per}_\ell(x) \]

has spectrum exactly \(S_L\): all points lie on cycles of permitted lengths, and every permitted length occurs. For any \(N\ge1\), the sentence

\[ \forall x\, f^N(x)=f^{N-1}(x)\quad\land\quad\exists x\,\Bigl(f^N(x)=f^{N-1}(x)\land\bigwedge_{0\le i<j<N}f^i(x)\ne f^j(x)\Bigr) \]

has spectrum exactly \(T_N\). Its universal conjunct bounds every orbit's preperiod by \(N-1\) and forces eventual period one; its existential conjunct requires a chain of \(N\) distinct points. A chain of that length plus any number of additional fixed points realizes every size \(n\ge N\). Finite unions are realized by disjunction, and the empty set by a contradiction. This proves the converse.

## Verification

The proof uses only the finite orbit-equality patterns of \(x,f(x),\ldots,f^d(x)\); no finite enumeration is used as an infinite proof. The tail construction is verified by adding incoming leaves without changing any existing forward orbit. The cycle construction has size \(s(L)+\sum k_\ell\ell\), with each \(k_\ell\ge0\), and the tail construction has minimum size \(N\) and admits every larger size. Both directions of the classification are therefore accounted for.

The class is a proper subfamily of all spectra in the one-function language. Every tail and every \(S_L\) is closed under multiplication by positive integers, and so is every finite union of them. In contrast, the odd positive integers are a spectrum in full first-order logic with one unary function: require exactly one fixed point and require every nonfixed point to belong to a 2-cycle. That sentence needs two variable symbols; its spectrum is not closed under multiplication (for example, \(3\) is odd but \(2\cdot3\) is even). This demonstrates that the one-variable-symbol restriction is substantive.

## Relationship to prior work

Durand, Fagin, and Loescher prove that unrestricted first-order spectra over a single unary function are exactly the eventually periodic sets, equivalently finite unions of arithmetic progressions. Gurevich and Shelah extend eventual periodicity to monadic second-order formulas with one unary function and unary relation symbols. These are broader language/logic results; neither theorem, as stated in the inspected main theorem and proof, gives the exact spectrum family for the one-variable-symbol fragment. The present classification refines those results by identifying the precise cycle-length semigroups and tails available under the variable restriction.

The phrase “one variable” is potentially ambiguous in this literature: a related Grandjean result concerns a one-universal-quantifier fragment, which is not the same restriction as allowing only one variable symbol. No claim is made about signatures with constants, additional functions, or additional relation symbols.

## Limitations

The classification is restricted to the signature \(\{f\}\) with equality, no constants, and nonempty finite structures. It does not classify spectra when extra symbols are added, and it does not provide a complexity bound for deciding equivalence of arbitrary input sentences. The literature comparison was targeted rather than exhaustive; an unlocated publication giving the same one-variable-symbol classification remains a residual risk.

## References

1. A. Durand, R. Fagin, and B. Loescher, “Spectra with Only Unary Function Symbols,” in *Computer Science Logic (CSL ’97)*, Lecture Notes in Computer Science 1414, Springer, 1998, pp. 189–202. DOI: 10.1007/BFb0028015. The paper appeared at CSL ’97, held 23–29 August 1997. Open full text: https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-csl97.pdf.
2. Y. Gurevich and S. Shelah, “Spectra of Monadic Second-Order Formulas with One Unary Function,” *Proceedings of LICS 2003*, pp. 291–300. DOI: 10.1109/LICS.2003.1210069. Open full text: https://shelah.logic.at/files/132926/01210069.pdf.
3. E. Grandjean, “First-order spectra with one variable,” *Journal of Computer and System Sciences* 40(2) (1990), 136–153. This is cited only as a potentially ambiguous neighboring topic; the accessible related abstract describes a one-universal-quantifier fragment, not the one-variable-symbol fragment used here.
