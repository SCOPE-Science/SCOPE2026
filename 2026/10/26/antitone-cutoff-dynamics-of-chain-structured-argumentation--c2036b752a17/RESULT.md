# Antitone cutoff dynamics of chain-structured argumentation

## Finding
For each integer \(n\ge 1\), consider a finite subargument argumentation framework on \(A=\{1,\ldots,n\}\) in which argument \(i\) is a direct proper subargument of \(i+1\), and the directed direct-attack relation \(D\subseteq A\times A\) is arbitrary (including possibly empty and self-attacks). The complete extensions have an exact description by the two-cycles of a nonincreasing cutoff function. There is exactly one preferred extension, at most one stable extension, and at most \(\lfloor n/2\rfloor+1\) complete extensions; the last bound is sharp for every \(n\). The possible cutoff functions number exactly \(\binom{2n}{n}\), and exactly \(\binom{2n-1}{n}\) of their profiles admit a stable extension.

More precisely, put \(t_i=\min\{j:(i,j)\in D\}\) if row \(i\) contains an attack and put \(t_i=n+1\) otherwise. Define \(h:\{0,\ldots,n\}\to\{0,\ldots,n\}\) by
\[
h(0)=n,\qquad h(k)=\min_{1\le i\le k} t_i-1\quad(1\le k\le n).
\]
For prefixes \(E_k=\{1,\ldots,k\}\), with \(E_0=\varnothing\), the complete-extension indices are **exactly**
\[
\big\{k:h(h(k))=k\ \text{and}\ h(k)\ge k\big\}.
\]
The stable-extension indices are **exactly** \(\{k:h(k)=k\}\). Their position-refined census among all cutoff profiles is
\[
\#\{h:h(k)=k\}=\binom{n-1}{k-1}\binom nk\quad(1\le k\le n).
\]
A profile means the cutoff function \(h\), not an isomorphism class of frameworks and not an extension-equivalence class.

## Assumptions and scope
The subargument relation has the direct arcs \((i,i+1)\) for \(1\le i<n\), so the reflexive-transitive subargument closure of \(j\) is the prefix \(E_j\). Direct attack \(D\) is any subset of \(A\times A\). The semantics are the structure-sensitive definitions of Liao (arXiv:2601.12038v3): an argument is defended by \(E\) when every direct attacker of any of its subarguments is counterattacked by some member of \(E\) on one of that attacker's subarguments. Conflict-freeness tests all subarguments of accepted arguments; admissibility additionally requires subargument closure and defence of accepted arguments; completeness requires admission of all defended arguments. Stable extensions additionally attack every argument outside them through its subarguments. Grounded and preferred refer to the least and maximal complete extensions, respectively.

Every argumentation framework here has at least one complete extension. No acyclicity is imposed on \(D\), and no claim is made for arbitrary branching subargument posets, multichain structures, or non-SAF attack semantics.

## Proof
**Step 1: A single threshold records attack propagation.** Because the subarguments of \(j\) form \(E_j\), a direct attacker \(i\) attacks some subargument of \(j\) exactly when \(t_i\le j\). The set of arguments attacked by the accepted prefix \(E_k\) is therefore
\[
E_k^+=\{h(k)+1,\ldots,n\}.
\]
Here the suffix is empty when \(h(k)=n\). Consequently \(E_k\) is structure-conflict-free precisely when \(h(k)\ge k\).

**Step 2: The defense map is the square of the cutoff.** An attacker \(i\) of a subargument of \(j\) has \(t_i\le j\). It is counterattacked by \(E_k\) exactly when \(i>h(k)\), by Step 1 applied to the attacker's subarguments. Thus \(j\) is defended by \(E_k\) if and only if no \(i\le h(k)\) has \(t_i\le j\), equivalently \(j\le h(h(k))\). Hence
\[
\operatorname{Def}(E_k)=E_{h(h(k))}.
\]
The subargument-closure condition forces every admissible set to be a prefix. A prefix is complete precisely when it is conflict-free and equals its defended set, giving the displayed complete-extension criterion. It is stable precisely when it attacks all omitted arguments, i.e. when \(h(k)\le k\), while conflict-freeness forces \(h(k)\ge k\); therefore stability is equivalent to \(h(k)=k\).

**Step 3: Uniqueness and the sharp extension bound.** The function \(h\) is nonincreasing. Hence it has at most one fixed point and its two-cycles consist of pairs \(k<\ell\) with \(h(k)=\ell\) and \(h(\ell)=k\). Each such two-cycle contributes exactly its lower state \(k\) as a complete extension (the upper state is not conflict-free). A fixed point, when present, contributes one additional complete extension. Distinct cycles are disjoint subsets of the \(n+1\) states, so at most \(\lceil(n+1)/2\rceil=\lfloor n/2\rfloor+1\) complete extensions occur. All complete extensions are prefixes, so they are nested; their largest is the unique preferred extension, and the smallest is grounded. If the stable extension exists, it is the unique preferred extension.

The bound is attained by putting exactly one direct attack in row \(i\), targeting \(n+1-i\). Then \(h(k)=n-k\), and exactly the prefixes \(E_k\) with \(0\le k\le\lfloor n/2\rfloor\) are complete. A stable extension occurs for this example precisely when \(n\) is even.

**Step 4: Realization and exact profile census.** Conversely, any nonincreasing \(h\) from \(\{0,\ldots,n\}\) to itself with \(h(0)=n\) is realized: in row \(i\), place only the direct attack on target \(h(i)+1\) when \(h(i)<n\), otherwise leave the row empty. Prefix minima then give the prescribed \(h\). The \(n\) remaining values \(h(1),\ldots,h(n)\) form a weakly decreasing sequence from \(0\) to \(n\), of which there are \(\binom{2n}{n}\).

For fixed \(1\le k\le n\), imposing \(h(k)=k\) leaves \(k-1\) weakly decreasing values from \(k\) to \(n\), with \(\binom{n-1}{k-1}\) choices, and \(n-k\) values from \(0\) to \(k\), with \(\binom nk\) choices. By uniqueness of the fixed point these cases are disjoint. Vandermonde's identity gives
\[
\sum_{k=1}^n\binom{n-1}{k-1}\binom nk=\binom{2n-1}{n}=\tfrac12\binom{2n}{n}.
\]
This completes the classifications and counts for every \(n\ge1\).

## Verification
Run the accompanying standalone, standard-library-only \(\texttt{checker.py}\) with \(\texttt{python checker.py}\). It evaluates the original structural-conflict, defense and stable definitions directly over all \(2^{n^2}\) direct-attack relations for \(1\le n\le4\) (66,066 relations), then on 600 deterministic sampled relations for \(5\le n\le8\). It also enumerates all 17,576 nonincreasing cutoff profiles for \(1\le n\le8\), verifies the stable-position binomial census, half-stable identity and the sharp anticorrelated witness. The recorded run finished with \(\texttt{ALL_CHECKS_OK}\) and 1,019,526 tracked assertions. These finite checks test the definitions and proof; they are not a substitute for the all-size argument above.

## Relationship to prior work
Liao (2026) supplies the definitions of subargument argumentation frameworks, defense, fixed-point complete extensions, and extension-preserving projection into standard Dung frameworks. Our proof specializes those definitions to one **total** subargument chain; the explicit antitone cutoff dynamics, sharp complete-extension bound and exact fraction of stable profiles are the additional claims. Prakken (2010) proves general results on structured arguments and subargument closure, but the inspected sections do not give this cutoff classification. Ferrers and threshold digraphs have nested adjacency rows (Reilly, Scheinerman and Zhang, 2014); a graph-theoretic characterization of such rows alone does not provide their SAF complete, preferred or stable semantics. No claim of originality is made for the general fixed-point theorem, the abstract Ferrers description or the elementary binomial identities used to enumerate the profiles.

## Limitations
The result assumes one reflexive-transitive **total chain** of subarguments, all finite argument sets, and the cited structure-sensitive semantics. The count of \(\binom{2n}{n}\) is of distinct cutoff functions; many different raw attack relations induce the same function, and different cutoff functions may induce the same set of extensions. Prior work on Ferrers digraph kernels or specialized argumentation semantics under other terminology could contain a comparable result; this is a priority risk. Exhaustive computation ends at size four for raw attacks and size eight for cutoff profiles. Independent verification has not been performed.

## References
- Beishui Liao, *Subargument Argumentation Frameworks: Separating Direct Conflict from Structural Dependency*, arXiv:2601.12038v3, 2026. First public preprint 2026-01-17; version 3 dated 2026-04-13. https://arxiv.org/abs/2601.12038
- Henry Prakken, *An abstract framework for argumentation with structured arguments*, *Argument & Computation* 1 (2010), 93--124, DOI:10.1080/19462160903564592.
- Elizabeth Reilly, Edward Scheinerman, and Yiguang Zhang, *Random Threshold Digraphs*, *Electronic Journal of Combinatorics* 21(2) (2014), #P2.48, DOI:10.37236/4050.
