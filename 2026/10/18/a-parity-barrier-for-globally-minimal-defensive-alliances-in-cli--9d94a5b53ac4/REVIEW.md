# Independent mathematical audit

## correctness

PASS

Every selected peripheral of a hub-free S in blade i has s_i-1 allies and degree m_i, so defense iff s_i>=k_i+1; inclusion minimality forces a single blade with exactly k_i+1 members. With hub selected, each selected peripheral needs s_i>=k_i; if any s_i>=k_i+1 a proper hub-free alliance exists. Hence minimal hub sets have s_i=0 or k_i; hub defense needs x=sum s_i>=floor(M/2), while maximum sum k_i=(M-o)/2=floor(M/2)-floor(o/2). This forces o<=1 and all s_i=k_i (since k_i>=1). Conversely tight hub-containing sets have no defending proper subset: dropping hub leaves too few per blade and dropping any peripheral violates hub threshold. Counting subsets gives sum_i C(m_i,k_i+1)z^{k_i+1}+1_{o<=1} prod_i C(m_i,k_i)z^{1+floor M/2}. Even uniform m_i=2k allows hub size rk+1, odd m_i=2k+1 prevents it and has upper k+1; drop (r-1)k. Independently exhaustive all-subsets/all proper suballiance checks on eight small mixed even/odd clique windmills reproduced exactly the set masks and polynomial. The finite test corroborates the universal inequality proof and is not an infinite proof.

## originality

PASS

No inspected result implies the entire final claim on the same mathematical objects and hypotheses; the established machinery and access risks are credited explicitly. Best-of-knowledge, not a definitive priority certificate.

## value

PASS

The one-hub multi-clique family is a natural network class whose global inclusion-minimal alliance enumeration is sensitive to blade parity. Complete classification and arbitrarily long gaps of attainable minimal sizes give an exact structural answer for a recognized graph alliance invariant, not a trivial table or a generic alliance-algorithm restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
