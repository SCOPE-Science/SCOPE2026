# Independent mathematical audit

## correctness

PASS

Independently recovered the joint order and tree law: with seen set S, current x and u=n−|S|, a specified next new label y with predecessor z∈S has probability (1+u·1[z=x])/(nu). The immediate jump contributes 1/n only for z=x; summing strings of one or more old draws ending at z contributes 1/(nu). Multiplication yields the stated order weights times a common factor, with the first root discovery contributing a common numerator n. For the permutation expansion, remove the ancestor-closed prefix, write a=τ_i and b=τ_{i+1}. In a valid suffix input the first scanned symbol has b as its first available ancestor in the forest without a. Reinserting a later than first prepends a to that first chain exactly when p(b)=a; otherwise b would precede a. Reinserting a first always works since a has no un-emitted ancestor. Erasing a preserves the shorter expansion, so this induction exhausts the distinct input permutations, giving exactly the displayed product. The latest scanned leaf is the latest output: leaves cannot be emitted earlier, and every internal vertex precedes an output descendant leaf. Uniform permutations assign each leaf probability 1/|Λ(T)|. This also covers k=1, a unique leaf, and suppression of holding steps.

## originality

PASS

The contribution is the fixed-tree terminal marginal and its leaf-refined fiber identity. Zheng already gives the full weighted order law and total normalization and explicitly leaves later-position marginals for analysis; the inspected sources do not derive the uniform terminal-leaf marginal.

## value

PASS

It evaluates a concrete outstanding marginal of the complete-graph order law, nontrivially independent of asymmetries of the fixed tree. The permutation lift both explains the marginal and realizes all weights, rather than recomputing isolated trees or invoking nonexistent leaf symmetry of the conditioned tree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
