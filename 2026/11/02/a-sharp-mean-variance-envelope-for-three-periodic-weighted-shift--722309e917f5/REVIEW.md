# Independent mathematical audit

## correctness

PASS

For nonnegative three-periodic unilateral shift weights a,b,c, grouping residue coordinates bounds numerical radius by the Perron root of the half-weighted symmetric triangle; repeating its eigenvector across N periods proves the reverse bound, including zero weights. Writing L=2w, P=(S^2+Q)/3, R=abc gives L^3-PL-2R=0; the largest positive root increases strictly with R. Exact fixed-sum/fixed-second-moment minimization of abc yields the two-equal small-variance branch for q<1/2 and a zero-weight branch for q>=1/2, with all boundary equality cases. Rationalizing [F(q)-1/3]/q shows its minimum at q=1/2 and optimal linear stability coefficient 1/sqrt(2)-2/3. Independent NumPy diagonalization verified both lower bounds on 999 nonzero integer triples; this is corroboration only, not proof for every real triple.

## originality

PASS

Bounded best-of-knowledge scientific comparison: An arithmetic mean lower bound w>=S/3 is weaker than w>=SF(q) for q>0; knowing the cubic L^3-PL-2abc only allows the new formula after a nontrivial constrained product minimization and equality proof. Ridge general periodic formula does not by itself fix the product minimizers. The targeted Resultary query and primary works were compared on objects, hypotheses, implication and parameters, not simply titles. No decisive prior-coverage theorem identified; this is not a proof of historical priority.

## value

PASS

The first sharp fixed-mean/fixed-variance lower envelope for a natural three-periodic operator class is structurally motivated: variation around the arithmetic mean affects numerical radius, a basic operator norm proxy. The exact zero-weight support transition at q=1/2 and optimal uniform second-moment coefficient are nontrivial information not obtained from an unconditional mean bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
